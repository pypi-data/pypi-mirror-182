"""Functions required for RL algorithm"""

import copy

import numpy as np

import ambulance_game as abg


def utility_function_3(Qs, server_id, e_parameter=0.5):
    """
    Utility function 3 is the weighted average of the following:
        - The mean service time
        - The proportion of time the server was idle
    Here we iterate over all simulations to get the average of both the service
    time and the idle time for all values of the server with id "server_id".
    """
    server_all_simulations = [Q.nodes[2].servers[server_id - 1] for Q in Qs]
    mean_service_time = np.mean(
        [np.mean(srv.service_times) for srv in server_all_simulations]
    )
    idle_time = np.mean(
        [
            (Qs[Q_id].current_time - srv.busy_time) / Qs[Q_id].current_time
            for Q_id, srv in enumerate(server_all_simulations)
        ]
    )
    return e_parameter * mean_service_time + (1 - e_parameter) * idle_time


def pick_a_state(Q):
    """
    Pick a state to update.
    """
    all_states = Q.statetracker.state_probabilities()
    all_visited_states = [state for state in all_states if all_states[state] > 0]
    index_choice = np.random.randint(len(all_visited_states))
    state = all_visited_states[index_choice]
    return state


def pick_policy(Qs, rates, num_of_servers):
    """
    Pick a new policy for a single server.
    """
    new_rates = copy.deepcopy(rates)
    Q = np.random.choice(Qs)
    srv = np.random.randint(1, num_of_servers + 1)
    state = pick_a_state(Q)
    scale = np.random.uniform(0.5, 1.5)
    new_rates[srv][state] *= scale
    return new_rates, srv


def accept_policy(
    Qs, utility_function, e_parameter, server_utilities, current_server_id
):
    """
    Accept or reject a policy.
    """
    condition = server_utilities[current_server_id - 1] <= utility_function(
        Qs, current_server_id, e_parameter
    )
    return condition


def are_within_limits(rates):
    """
    Check if the rates are within the limits.
    """
    for srv in rates:
        for state in rates[srv]:
            rate = rates[srv][state]
            if rate < 0.1 or rate > 1.3:
                print(f"Rate {rate} out of bounds: Server {srv}, State {state}")
                return False
    return True


def update_server_utilities(Qs, utility_function, e_parameter, num_of_servers):
    """
    Update the utilities of all servers.
    """
    new_utilities = [
        utility_function(Qs, srv_id, e_parameter)
        for srv_id in range(1, num_of_servers + 1)
    ]
    return new_utilities


def run_simulation(parameters, rates):
    """
    Run the simulation
    """
    simulations = abg.simulation.simulate_model(
        lambda_1=parameters["lambda_1"],
        lambda_2=parameters["lambda_2"],
        mu=rates,
        num_of_servers=parameters["num_of_servers"],
        threshold=parameters["threshold"],
        system_capacity=parameters["system_capacity"],
        buffer_capacity=parameters["buffer_capacity"],
        runtime=parameters["runtime"],
        num_of_trials=parameters["num_of_trials"],
        seed_num=parameters["seed_num"],
        server_priority_function=parameters["server_priority_function"],
    )
    if type(simulations) is not list:
        simulations = [simulations]
    return simulations


def output_to_file(utilist, filename="demo.csv"):
    with open(filename, "a") as f:
        f.write(utilist + "\n")


def output_to_json_file(utilist, filename="demo.json"):
    with open(filename, "a") as f:
        f.write(utilist + "\n")
