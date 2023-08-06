"""
Tests for the waiting time functionality
"""
import numpy as np

from ambulance_game.markov.waiting import (
    get_mean_waiting_time_using_markov_state_probabilities,
    get_waiting_time_for_each_state_recursively,
    mean_waiting_time_formula_using_closed_form_approach,
    mean_waiting_time_formula_using_direct_approach,
    mean_waiting_time_formula_using_recursive_approach,
    overall_waiting_time_formula,
)

NUMBER_OF_DIGITS_TO_ROUND = 8


def test_get_waiting_time_of_each_state_recursively_class_1_property():
    """
    This test ensures that no matter what row we are on in the Markov model, it
    doesn't make a difference from the perspective of a class 1 individual.
    """
    for u in range(6):
        wait_on_state = get_waiting_time_for_each_state_recursively(
            state=(u, 5),
            class_type=0,
            lambda_2=1,
            lambda_1=1,
            mu=2,
            num_of_servers=3,
            threshold=1,
            system_capacity=6,
            buffer_capacity=6,
        )
        assert wait_on_state == 1 / 3, u


def test_get_waiting_time_of_each_state_recursively_class_2_property():
    """
    This test ensures that no matter what row or column we are on in the Markov
    model, when that the column is greater than the threshold it doesn't make a
    difference from the perspective of a class 2 individual.
    """
    for u in range(1, 5):
        for v in range(4, 6):
            wait_on_state = get_waiting_time_for_each_state_recursively(
                state=(u, v),
                class_type=1,
                lambda_2=1,
                lambda_1=1,
                mu=2,
                num_of_servers=3,
                threshold=4,
                system_capacity=6,
                buffer_capacity=6,
            )
            assert wait_on_state == 1 / 6, (u, v)


def test_mean_waiting_time_formula_using_recursive_for_class_1_individuals_example():
    """
    Test for the recursive formula for the mean waiting time for class 1 individuals
    """
    all_states = [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 2),
        (3, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
    ]
    pi = np.array(
        [
            [0.09375, 0.1875, 0.1875, 0.0625],
            [np.nan, np.nan, 0.125, 0.0625],
            [np.nan, np.nan, 0.09375, 0.05208333],
            [np.nan, np.nan, 0.07291667, 0.0625],
        ]
    )

    mean_wait = mean_waiting_time_formula_using_recursive_approach(
        all_states=all_states,
        pi=pi,
        class_type=0,
        lambda_1=1,
        lambda_2=1,
        mu=1,
        num_of_servers=2,
        threshold=2,
        system_capacity=3,
        buffer_capacity=3,
    )

    assert round(mean_wait, NUMBER_OF_DIGITS_TO_ROUND) == round(
        0.31506849396134357, NUMBER_OF_DIGITS_TO_ROUND
    )


def test_mean_waiting_time_formula_using_recursive_for_class_2_individuals_example():
    """
    Test for the recursive formula for the mean waiting time for class 2 individuals
    """
    all_states = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
    ]
    pi = np.array(
        [
            [0.11428571, 0.22857143, 0.22857143, 0.22857143],
            [np.nan, np.nan, np.nan, 0.11428571],
            [np.nan, np.nan, np.nan, 0.05714286],
            [np.nan, np.nan, np.nan, 0.02857143],
        ]
    )

    mean_wait = mean_waiting_time_formula_using_recursive_approach(
        all_states=all_states,
        pi=pi,
        class_type=1,
        lambda_1=1,
        lambda_2=1,
        mu=1,
        num_of_servers=2,
        threshold=3,
        system_capacity=3,
        buffer_capacity=3,
    )

    assert round(mean_wait, NUMBER_OF_DIGITS_TO_ROUND) == round(
        0.32352941297577853, NUMBER_OF_DIGITS_TO_ROUND
    ), mean_wait


def test_mean_waiting_time_formula_using_direct_for_class_1_individuals_example():
    """
    Test for the direct formula for the mean waiting time for class 1 individuals
    """
    all_states = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
    ]
    pi = np.array(
        [
            [0.11428571, 0.22857143, 0.22857143, 0.22857143],
            [np.nan, np.nan, np.nan, 0.11428571],
            [np.nan, np.nan, np.nan, 0.05714286],
            [np.nan, np.nan, np.nan, 0.02857143],
        ]
    )

    mean_wait = mean_waiting_time_formula_using_direct_approach(
        all_states=all_states,
        pi=pi,
        class_type=0,
        lambda_1=1,
        lambda_2=1,
        mu=1,
        num_of_servers=2,
        threshold=3,
        system_capacity=3,
        buffer_capacity=3,
    )

    assert round(mean_wait, NUMBER_OF_DIGITS_TO_ROUND) == round(
        0.20000000175, NUMBER_OF_DIGITS_TO_ROUND
    )


def test_mean_waiting_time_formula_using_direct_for_class_2_individuals_example():
    """
    Test for the direct formula for the mean waiting time for class 2 individuals
    """
    all_states = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
    ]
    pi = np.array(
        [
            [0.11428571, 0.22857143, 0.22857143, 0.22857143],
            [np.nan, np.nan, np.nan, 0.11428571],
            [np.nan, np.nan, np.nan, 0.05714286],
            [np.nan, np.nan, np.nan, 0.02857143],
        ]
    )

    mean_wait = mean_waiting_time_formula_using_direct_approach(
        all_states=all_states,
        pi=pi,
        class_type=1,
        lambda_1=1,
        lambda_2=1,
        mu=1,
        num_of_servers=2,
        threshold=3,
        system_capacity=3,
        buffer_capacity=3,
    )

    assert round(mean_wait, NUMBER_OF_DIGITS_TO_ROUND) == round(
        0.32352941297577853, NUMBER_OF_DIGITS_TO_ROUND
    )


def test_mean_waiting_time_formula_using_closed_form_for_class_1_individuals_example():
    """
    Test for the closed-form formula for the mean waiting time for class 1 individuals
    """
    all_states = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (0, 4),
        (1, 4),
        (2, 4),
    ]
    pi = np.array(
        [
            [0.08695652, 0.17391304, 0.17391304, 0.17391304, 0.05797101],
            [np.nan, np.nan, np.nan, 0.11594203, 0.05797101],
            [np.nan, np.nan, np.nan, 0.08695652, 0.07246377],
        ]
    )
    mean_wait = mean_waiting_time_formula_using_closed_form_approach(
        all_states=all_states,
        pi=pi,
        class_type=0,
        lambda_1=1,
        lambda_2=1,
        mu=1,
        num_of_servers=2,
        threshold=3,
        system_capacity=4,
        buffer_capacity=2,
    )
    assert round(mean_wait, NUMBER_OF_DIGITS_TO_ROUND) == round(
        0.5714285731887755, NUMBER_OF_DIGITS_TO_ROUND
    )


def test_mean_waiting_time_formula_using_closed_form_for_class_2_individuals_example():
    """
    Test for the closed-form formula for the mean waiting time for class 2 individuals
    """
    all_states = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (1, 4),
        (2, 4),
    ]
    pi = np.array(
        [
            [0.0952381, 0.19047619, 0.19047619, 0.19047619, 0.19047619],
            [np.nan, np.nan, np.nan, np.nan, 0.0952381],
            [np.nan, np.nan, np.nan, np.nan, 0.04761905],
        ]
    )
    mean_wait = mean_waiting_time_formula_using_closed_form_approach(
        all_states=all_states,
        pi=pi,
        class_type=1,
        lambda_1=1,
        lambda_2=1,
        mu=1,
        num_of_servers=2,
        threshold=4,
        system_capacity=4,
        buffer_capacity=2,
    )
    assert round(mean_wait, NUMBER_OF_DIGITS_TO_ROUND) == round(
        0.59999999895, NUMBER_OF_DIGITS_TO_ROUND
    ), mean_wait


def test_overall_waiting_time_formula_example():
    """
    Test that the overall mean waiting formula returns the same expected output
    when using both the recursive approach and the closed-form one
    """
    all_states = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (1, 4),
        (2, 4),
    ]
    pi = np.array(
        [
            [0.0952381, 0.19047619, 0.19047619, 0.19047619, 0.19047619],
            [np.nan, np.nan, np.nan, np.nan, 0.0952381],
            [np.nan, np.nan, np.nan, np.nan, 0.04761905],
        ]
    )
    mean_overall_recursive_wait = overall_waiting_time_formula(
        all_states=all_states,
        pi=pi,
        lambda_1=1,
        lambda_2=2,
        mu=1,
        num_of_servers=2,
        threshold=4,
        system_capacity=4,
        buffer_capacity=2,
        waiting_formula=mean_waiting_time_formula_using_recursive_approach,
    )

    mean_overall_closed_form_wait = overall_waiting_time_formula(
        all_states=all_states,
        pi=pi,
        lambda_1=1,
        lambda_2=2,
        mu=1,
        num_of_servers=2,
        threshold=4,
        system_capacity=4,
        buffer_capacity=2,
        waiting_formula=mean_waiting_time_formula_using_closed_form_approach,
    )

    assert (
        round(mean_overall_recursive_wait, NUMBER_OF_DIGITS_TO_ROUND)
        == round(mean_overall_closed_form_wait, NUMBER_OF_DIGITS_TO_ROUND)
        == round(0.5555555540432099, NUMBER_OF_DIGITS_TO_ROUND)
    ), (mean_overall_recursive_wait, mean_overall_closed_form_wait)


def test_get_mean_waiting_time_example_1():
    """
    Example on getting the mean waiting time recursively from the Markov chain
    """
    mean_waiting_time = get_mean_waiting_time_using_markov_state_probabilities(
        lambda_2=0.2,
        lambda_1=0.2,
        mu=0.2,
        num_of_servers=3,
        threshold=4,
        system_capacity=10,
        buffer_capacity=10,
        class_type=0,
        waiting_formula=mean_waiting_time_formula_using_recursive_approach,
    )
    assert round(mean_waiting_time, NUMBER_OF_DIGITS_TO_ROUND) == round(
        1.472071670896375, NUMBER_OF_DIGITS_TO_ROUND
    )


def test_get_mean_waiting_time_example_2():
    """
    Example on getting the mean waiting time recursively from the Markov chain
    """
    mean_waiting_time = get_mean_waiting_time_using_markov_state_probabilities(
        lambda_2=0.2,
        lambda_1=0.2,
        mu=0.2,
        num_of_servers=3,
        threshold=4,
        system_capacity=10,
        buffer_capacity=10,
        class_type=1,
        waiting_formula=mean_waiting_time_formula_using_recursive_approach,
    )
    assert round(mean_waiting_time, NUMBER_OF_DIGITS_TO_ROUND) == round(
        0.7377914457854086, NUMBER_OF_DIGITS_TO_ROUND
    )


def test_get_mean_waiting_time_example_3():
    """
    Example on getting the mean waiting time recursively from the Markov chain
    """
    mean_waiting_time = get_mean_waiting_time_using_markov_state_probabilities(
        lambda_2=0.2,
        lambda_1=0.2,
        mu=0.2,
        num_of_servers=3,
        threshold=3,
        system_capacity=10,
        buffer_capacity=10,
        class_type=1,
        waiting_formula=mean_waiting_time_formula_using_recursive_approach,
    )
    assert mean_waiting_time == 0


def test_get_mean_waiting_time_example_4():
    """
    Example on getting the mean waiting time recursively from the Markov chain
    """
    mean_waiting_time = get_mean_waiting_time_using_markov_state_probabilities(
        lambda_2=0.2,
        lambda_1=0.2,
        mu=0.2,
        num_of_servers=3,
        threshold=4,
        system_capacity=10,
        buffer_capacity=10,
        class_type=None,
        waiting_formula=mean_waiting_time_formula_using_recursive_approach,
    )
    assert round(mean_waiting_time, NUMBER_OF_DIGITS_TO_ROUND) == round(
        1.1051493390764142, NUMBER_OF_DIGITS_TO_ROUND
    )


def test_get_mean_waiting_time_example_5():
    """
    Example on getting the mean waiting time from a closed form formula
    """
    mean_waiting_time = get_mean_waiting_time_using_markov_state_probabilities(
        lambda_2=0.2,
        lambda_1=0.2,
        mu=0.2,
        num_of_servers=3,
        threshold=4,
        system_capacity=10,
        buffer_capacity=10,
        class_type=0,
        waiting_formula=mean_waiting_time_formula_using_closed_form_approach,
    )
    assert round(mean_waiting_time, NUMBER_OF_DIGITS_TO_ROUND) == round(
        1.4720716708963748, NUMBER_OF_DIGITS_TO_ROUND
    )


def test_get_mean_waiting_time_example_6():
    """
    Example on getting the mean waiting time from a closed form formula
    """
    mean_waiting_time = get_mean_waiting_time_using_markov_state_probabilities(
        lambda_2=0.2,
        lambda_1=0.2,
        mu=0.2,
        num_of_servers=3,
        threshold=4,
        system_capacity=10,
        buffer_capacity=10,
        class_type=1,
        waiting_formula=mean_waiting_time_formula_using_closed_form_approach,
    )
    assert round(mean_waiting_time, NUMBER_OF_DIGITS_TO_ROUND) == round(
        0.7377914457854088, NUMBER_OF_DIGITS_TO_ROUND
    )


def test_get_mean_waiting_time_example_7():
    """
    Example on getting the mean waiting time from a closed form formula
    """
    mean_waiting_time = get_mean_waiting_time_using_markov_state_probabilities(
        lambda_2=0.2,
        lambda_1=0.2,
        mu=0.2,
        num_of_servers=3,
        threshold=3,
        system_capacity=10,
        buffer_capacity=10,
        class_type=1,
        waiting_formula=mean_waiting_time_formula_using_closed_form_approach,
    )
    assert mean_waiting_time == 0


def test_get_mean_waiting_time_example_8():
    """
    Example on getting the mean waiting time from a closed form formula
    """
    mean_waiting_time = get_mean_waiting_time_using_markov_state_probabilities(
        lambda_2=0.2,
        lambda_1=0.2,
        mu=0.2,
        num_of_servers=3,
        threshold=4,
        system_capacity=10,
        buffer_capacity=10,
        class_type=None,
        waiting_formula=mean_waiting_time_formula_using_closed_form_approach,
    )
    assert round(mean_waiting_time, NUMBER_OF_DIGITS_TO_ROUND) == round(
        1.1051493390764142, NUMBER_OF_DIGITS_TO_ROUND
    )


def test_get_mean_waiting_time_example_9():
    """
    Example on getting the mean waiting time from a closed form formula
    """
    mean_waiting_time = get_mean_waiting_time_using_markov_state_probabilities(
        lambda_2=0.2,
        lambda_1=0.2,
        mu=0.2,
        num_of_servers=3,
        threshold=4,
        system_capacity=10,
        buffer_capacity=10,
        class_type=None,
        waiting_formula=mean_waiting_time_formula_using_direct_approach,
    )
    assert round(mean_waiting_time, NUMBER_OF_DIGITS_TO_ROUND) == round(
        1.1051493390764142, NUMBER_OF_DIGITS_TO_ROUND
    )
