"""
Code for custom distribution classes and other distribution related functions
"""

import random

import ciw


class StateDependentExponential(
    ciw.dists.Distribution
):  # pylint: disable=too-few-public-methods
    """
    A class that inherits from the `Distribution` class in the ciw module. This
    class is meant to be used in the simulation module as a state dependent
    distribution for the service of individuals.

    This distribution takes `rates` as an argument; a disctionary with keys
    states `(u,v)` and values the service rate at that state.
    """

    def __init__(self, rates):
        if any(rate <= 0 for rate in rates.values()):
            raise ValueError(
                "Exponential distribution must sample positive numbers only."
            )
        self.rates = rates

    def sample(self, t=None, ind=None):
        """
        This method is used to sample the service time for an individual based
        on the current state
        """
        state = (
            len(ind.simulation.nodes[1].individuals[0]),
            len(ind.simulation.nodes[2].individuals[0]),
        )
        is_invalid_state = state[0] > 0 and state[1] < ind.simulation.threshold
        if is_invalid_state:
            state = (state[0] - 1, state[1] + 1)
        rate = self.rates[state]
        return random.expovariate(rate)


class ServerDependentExponential(
    ciw.dists.Distribution
):  # pylint: disable=too-few-public-methods
    """
    A class that inherits from the `Distribution` class in the ciw module. This
    class is meant to be used in the simulation module as a server dependent
    distribution for the service of individuals.

    This distribution takes `rates` as an argument; a disctionary with keys
    server `k` and values the service rate for that server.
    """

    def __init__(self, rates):
        if any(rate <= 0 for rate in rates.values()):
            raise ValueError(
                "Exponential distribution must sample positive numbers only."
            )
        self.simulation = None
        self.rates = rates

    def sample(self, t=None, ind=None):
        """
        This method is used to sample the service time for an individual based
        on the server that the individual is assigned to
        """
        server = ind.server.id_number
        rate = self.rates[server]
        return random.expovariate(rate)


class StateServerDependentExponential(
    ciw.dists.Distribution
):  # pylint: disable=too-few-public-methods
    """
    A class that inherits from the `Distribution` class in the ciw module. This
    class is meant to be used in the simulation module as a state and server
    dependent distribution for the service of individuals.

    This distribution takes `rates` as an argument; a disctionary with keys
    server `k` and values another dictionary with keys the states and values the
    service rate for the particular server at that state.
    """

    def __init__(self, rates):
        for server_rates in rates.values():
            if any(rate <= 0 for rate in server_rates.values()):
                raise ValueError(
                    "Exponential distribution must sample positive numbers only."
                )
        self.simulation = None
        self.rates = rates

    def sample(self, t=None, ind=None):
        """
        This method is used to sample the service time for an individual based
        on the current state and the server that the individual is assigned to.
        The following steps are being executed:
            1. Find the server
            2. Find the state
            3. Check if the state is valid. Note that there are some cases where
                the visited state is not valid. These are the cases where the
                state `(u, T-1)` is visited where `u > 0`. This is meant to be
                an unreachable state. In such case remap the state to `(u+1, T)`
            4. Get the service rate for that server and state
            5. Sample the service time
            6. Update any possible attributes for the server
        """
        server = ind.server.id_number
        state = (
            len(ind.simulation.nodes[1].individuals[0]),
            len(ind.simulation.nodes[2].individuals[0]),
        )
        is_invalid_state = state[0] > 0 and state[1] < ind.simulation.threshold
        if is_invalid_state:
            state = (state[0] - 1, state[1] + 1)
        rate = self.rates[server][state]
        service_time = random.expovariate(rate)
        self.update_server_attributes(ind, service_time)
        return service_time

    def update_server_attributes(self, ind, service_time):
        """
        Updates the server's attributes
        """
        if hasattr(ind.server, "served_inds"):
            ind.server.served_inds.append(self.simulation.current_time)
        else:
            ind.server.served_inds = [self.simulation.current_time]

        if hasattr(ind.server, "service_times"):
            ind.server.service_times.append(service_time)
        else:
            ind.server.service_times = [service_time]


def is_state_dependent(mu: dict):
    """
    Check if mu is a dictionary with keys that are tuples of 2 integers and values
    that are floats or integers.
    """
    for key, value in mu.items():
        if (
            not isinstance(key, tuple)
            or len(key) != 2
            or not isinstance(key[0], int)
            or not isinstance(key[1], int)
            or not isinstance(value, (float, int))
        ):
            return False
    return True


def is_server_dependent(mu: dict):
    """
    Checks if mu is a dictionary with keys that are servers and values that are
    service rates.
    """
    for key, value in mu.items():
        if not isinstance(key, int) or not isinstance(value, (float, int)):
            return False
    return True


def is_state_server_dependent(mu: dict):
    """
    Checks if mu is a dictionary of distionaries. The keys are servers id and
    the values are another dictionary with keys the states and values the
    service rates.
    """
    for key, value in mu.items():
        if not isinstance(key, int) or not is_state_dependent(value):
            return False
    return True


def get_service_distribution(mu):
    """
    Get the service distribution out of:
        - ciw.dists.Exponential
        - StateDependentExponential
        - ServerDependentExponential
        - StateServerDependentExponential
    """
    if isinstance(mu, (float, int)):
        return ciw.dists.Exponential(mu)
    if isinstance(mu, dict):
        if is_state_dependent(mu):
            return StateDependentExponential(mu)
        if is_server_dependent(mu):
            return ServerDependentExponential(mu)
        if is_state_server_dependent(mu):
            return StateServerDependentExponential(mu)
    raise ValueError("mu must be either an integer or a dictionary")


def get_arrival_distribution(arrival_rate):
    """
    Get the arrival distribution given the arrival rate. This function was
    created in case the arrival rate is zero. In such a case we need to
    specify a distribution that does not generate any arrivals.

    Parameters
    ----------
    arrival_rate : float
        The arrival rate of the model

    Returns
    -------
    object
        A ciw object that contains the arrival distribution of the model
    """
    if arrival_rate > 0:
        return ciw.dists.Exponential(arrival_rate)
    if arrival_rate == 0:
        return ciw.dists.NoArrivals()
    raise ValueError("Arrival rate must be a positive number")
