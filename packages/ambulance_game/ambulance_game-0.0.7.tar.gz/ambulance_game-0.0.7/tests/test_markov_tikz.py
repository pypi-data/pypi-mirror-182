"""
Tests for generating tikz code for markov chains.
"""

# pylint: disable=line-too-long

from ambulance_game.markov.tikz import (
    build_body_of_tikz_spanning_tree,
    generate_code_for_tikz_figure,
    generate_code_for_tikz_spanning_trees_rooted_at_00,
    get_tikz_code_for_permutation,
)


def test_generate_code_for_tikz_figure_example_1():
    """
    Generate example tikz code for markov chain with 1 server, 1 system capacity,
    1 buffer capacity and 1 threshold.
    """
    tikz_code = generate_code_for_tikz_figure(
        num_of_servers=1, threshold=1, system_capacity=1, buffer_capacity=1
    )
    assert isinstance(tikz_code, str)
    assert (
        tikz_code
        == "\\begin{tikzpicture}[-, node distance = 1cm, auto]\n\\node[state] (u0v0) {(0,0)};\n\\node[state, right=of u0v0] (u0v1) {(0,1)};\n\\draw[->](u0v0) edge[bend left] node {\\( \\Lambda \\)} (u0v1);\n\\draw[->](u0v1) edge[bend left] node {\\(\\mu \\)} (u0v0);\n\\node[state, below=of u0v1] (u1v1) {(1,1)};\n\\draw[->](u0v1) edge[bend left] node {\\( \\lambda_2 \\)} (u1v1);\n\\draw[->](u1v1) edge[bend left] node {\\(\\mu \\)} (u0v1);\n\\end{tikzpicture}"
    )


def test_generate_code_for_tikz_figure_example_2():
    """
    Generate example tikz code for markov chain with 6 servers, 9 system capacity,
    1 buffer capacity and 10 threshold.
    """
    tikz_code = generate_code_for_tikz_figure(
        num_of_servers=6, threshold=10, system_capacity=9, buffer_capacity=1
    )
    assert isinstance(tikz_code, str)
    assert (
        tikz_code
        == "\\begin{tikzpicture}[-, node distance = 1cm, auto]\n\\node[state] (u0v0) {(0,0)};\n\\node[state, right=of u0v0] (u0v1) {(0,1)};\n\\draw[->](u0v0) edge[bend left] node {\\( \\Lambda \\)} (u0v1);\n\\draw[->](u0v1) edge[bend left] node {\\(\\mu \\)} (u0v0);\n\\node[state, right=of u0v1] (u0v2) {(0,2)};\n\\draw[->](u0v1) edge[bend left] node {\\( \\Lambda \\)} (u0v2);\n\\draw[->](u0v2) edge[bend left] node {\\(2\\mu \\)} (u0v1);\n\\node[state, right=of u0v2] (u0v3) {(0,3)};\n\\draw[->](u0v2) edge[bend left] node {\\( \\Lambda \\)} (u0v3);\n\\draw[->](u0v3) edge[bend left] node {\\(3\\mu \\)} (u0v2);\n\\node[state, right=of u0v3] (u0v4) {(0,4)};\n\\draw[->](u0v3) edge[bend left] node {\\( \\Lambda \\)} (u0v4);\n\\draw[->](u0v4) edge[bend left] node {\\(4\\mu \\)} (u0v3);\n\\node[state, right=of u0v4] (u0v5) {(0,5)};\n\\draw[->](u0v4) edge[bend left] node {\\( \\Lambda \\)} (u0v5);\n\\draw[->](u0v5) edge[bend left] node {\\(5\\mu \\)} (u0v4);\n\\node[state, right=of u0v5] (u0v6) {(0,6)};\n\\draw[->](u0v5) edge[bend left] node {\\( \\Lambda \\)} (u0v6);\n\\draw[->](u0v6) edge[bend left] node {\\(6\\mu \\)} (u0v5);\n\\node[state, right=of u0v6] (u0v7) {(0,7)};\n\\draw[->](u0v6) edge[bend left] node {\\( \\Lambda \\)} (u0v7);\n\\draw[->](u0v7) edge[bend left] node {\\(6\\mu \\)} (u0v6);\n\\node[state, right=of u0v7] (u0v8) {(0,8)};\n\\draw[->](u0v7) edge[bend left] node {\\( \\Lambda \\)} (u0v8);\n\\draw[->](u0v8) edge[bend left] node {\\(6\\mu \\)} (u0v7);\n\\node[state, right=of u0v8] (u0v9) {(0,9)};\n\\draw[->](u0v8) edge[bend left] node {\\( \\Lambda \\)} (u0v9);\n\\draw[->](u0v9) edge[bend left] node {\\(6\\mu \\)} (u0v8);\n\\node[state, below=of u0v9] (u1v9) {(1,9)};\n\\draw[->](u0v9) edge[bend left] node {\\( \\lambda_2 \\)} (u1v9);\n\\draw[->](u1v9) edge[bend left] node {\\(6\\mu \\)} (u0v9);\n\\end{tikzpicture}"
    )


def test_generate_code_for_tikz_figure_example_3():
    """
    Generate example tikz code for markov chain with 4 servers, 6 system capacity,
    2 buffer capacity and 6 threshold.
    """
    tikz_code = generate_code_for_tikz_figure(
        num_of_servers=4, threshold=6, system_capacity=6, buffer_capacity=2
    )
    assert isinstance(tikz_code, str)
    assert (
        tikz_code
        == "\\begin{tikzpicture}[-, node distance = 1cm, auto]\n\\node[state] (u0v0) {(0,0)};\n\\node[state, right=of u0v0] (u0v1) {(0,1)};\n\\draw[->](u0v0) edge[bend left] node {\\( \\Lambda \\)} (u0v1);\n\\draw[->](u0v1) edge[bend left] node {\\(\\mu \\)} (u0v0);\n\\node[state, right=of u0v1] (u0v2) {(0,2)};\n\\draw[->](u0v1) edge[bend left] node {\\( \\Lambda \\)} (u0v2);\n\\draw[->](u0v2) edge[bend left] node {\\(2\\mu \\)} (u0v1);\n\\node[state, right=of u0v2] (u0v3) {(0,3)};\n\\draw[->](u0v2) edge[bend left] node {\\( \\Lambda \\)} (u0v3);\n\\draw[->](u0v3) edge[bend left] node {\\(3\\mu \\)} (u0v2);\n\\node[state, right=of u0v3] (u0v4) {(0,4)};\n\\draw[->](u0v3) edge[bend left] node {\\( \\Lambda \\)} (u0v4);\n\\draw[->](u0v4) edge[bend left] node {\\(4\\mu \\)} (u0v3);\n\\node[state, right=of u0v4] (u0v5) {(0,5)};\n\\draw[->](u0v4) edge[bend left] node {\\( \\Lambda \\)} (u0v5);\n\\draw[->](u0v5) edge[bend left] node {\\(4\\mu \\)} (u0v4);\n\\node[state, right=of u0v5] (u0v6) {(0,6)};\n\\draw[->](u0v5) edge[bend left] node {\\( \\Lambda \\)} (u0v6);\n\\draw[->](u0v6) edge[bend left] node {\\(4\\mu \\)} (u0v5);\n\\node[state, below=of u0v6] (u1v6) {(1,6)};\n\\draw[->](u0v6) edge[bend left] node {\\( \\lambda_2 \\)} (u1v6);\n\\draw[->](u1v6) edge[bend left] node {\\(4\\mu \\)} (u0v6);\n\\node[state, below=of u1v6] (u2v6) {(2,6)};\n\\draw[->](u1v6) edge[bend left] node {\\( \\lambda_2 \\)} (u2v6);\n\\draw[->](u2v6) edge[bend left] node {\\(4\\mu \\)} (u1v6);\n\\end{tikzpicture}"
    )


def test_generate_code_for_tikz_figure_example_4():
    """
    Generate example tikz code for markov chain with 3 servers, 5 system capacity,
    2 buffer capacity and 2 threshold.
    """
    tikz_code = generate_code_for_tikz_figure(
        num_of_servers=3, threshold=2, system_capacity=5, buffer_capacity=2
    )
    assert isinstance(tikz_code, str)
    assert (
        tikz_code
        == "\\begin{tikzpicture}[-, node distance = 1cm, auto]\n\\node[state] (u0v0) {(0,0)};\n\\node[state, right=of u0v0] (u0v1) {(0,1)};\n\\draw[->](u0v0) edge[bend left] node {\\( \\Lambda \\)} (u0v1);\n\\draw[->](u0v1) edge[bend left] node {\\(\\mu \\)} (u0v0);\n\\node[state, right=of u0v1] (u0v2) {(0,2)};\n\\draw[->](u0v1) edge[bend left] node {\\( \\Lambda \\)} (u0v2);\n\\draw[->](u0v2) edge[bend left] node {\\(2\\mu \\)} (u0v1);\n\\node[state, below=of u0v2] (u1v2) {(1,2)};\n\\draw[->](u0v2) edge[bend left] node {\\( \\lambda_2 \\)} (u1v2);\n\\draw[->](u1v2) edge[bend left] node {\\(2\\mu \\)} (u0v2);\n\\node[state, below=of u1v2] (u2v2) {(2,2)};\n\\draw[->](u1v2) edge[bend left] node {\\( \\lambda_2 \\)} (u2v2);\n\\draw[->](u2v2) edge[bend left] node {\\(2\\mu \\)} (u1v2);\n\\node[state, right=of u0v2] (u0v3) {(0,3)};\n\\draw[->](u0v2) edge[bend left] node {\\( \\lambda_1 \\)} (u0v3);\n\\draw[->](u0v3) edge[bend left] node {\\(3\\mu \\)} (u0v2);\n\\node[state, right=of u1v2] (u1v3) {(1,3)};\n\\draw[->](u1v2) edge[bend left] node {\\( \\lambda_1 \\)} (u1v3);\n\\draw[->](u1v3) edge[bend left] node {\\(3\\mu \\)} (u1v2);\n\\draw[->](u0v3) edge node {\\( \\lambda_2 \\)} (u1v3);\n\\node[state, right=of u2v2] (u2v3) {(2,3)};\n\\draw[->](u2v2) edge[bend left] node {\\( \\lambda_1 \\)} (u2v3);\n\\draw[->](u2v3) edge[bend left] node {\\(3\\mu \\)} (u2v2);\n\\draw[->](u1v3) edge node {\\( \\lambda_2 \\)} (u2v3);\n\\node[state, right=of u0v3] (u0v4) {(0,4)};\n\\draw[->](u0v3) edge[bend left] node {\\( \\lambda_1 \\)} (u0v4);\n\\draw[->](u0v4) edge[bend left] node {\\(3\\mu \\)} (u0v3);\n\\node[state, right=of u1v3] (u1v4) {(1,4)};\n\\draw[->](u1v3) edge[bend left] node {\\( \\lambda_1 \\)} (u1v4);\n\\draw[->](u1v4) edge[bend left] node {\\(3\\mu \\)} (u1v3);\n\\draw[->](u0v4) edge node {\\( \\lambda_2 \\)} (u1v4);\n\\node[state, right=of u2v3] (u2v4) {(2,4)};\n\\draw[->](u2v3) edge[bend left] node {\\( \\lambda_1 \\)} (u2v4);\n\\draw[->](u2v4) edge[bend left] node {\\(3\\mu \\)} (u2v3);\n\\draw[->](u1v4) edge node {\\( \\lambda_2 \\)} (u2v4);\n\\node[state, right=of u0v4] (u0v5) {(0,5)};\n\\draw[->](u0v4) edge[bend left] node {\\( \\lambda_1 \\)} (u0v5);\n\\draw[->](u0v5) edge[bend left] node {\\(3\\mu \\)} (u0v4);\n\\node[state, right=of u1v4] (u1v5) {(1,5)};\n\\draw[->](u1v4) edge[bend left] node {\\( \\lambda_1 \\)} (u1v5);\n\\draw[->](u1v5) edge[bend left] node {\\(3\\mu \\)} (u1v4);\n\\draw[->](u0v5) edge node {\\( \\lambda_2 \\)} (u1v5);\n\\node[state, right=of u2v4] (u2v5) {(2,5)};\n\\draw[->](u2v4) edge[bend left] node {\\( \\lambda_1 \\)} (u2v5);\n\\draw[->](u2v5) edge[bend left] node {\\(3\\mu \\)} (u2v4);\n\\draw[->](u1v5) edge node {\\( \\lambda_2 \\)} (u2v5);\n\\end{tikzpicture}"
    )


def test_build_body_of_tikz_spanning_tree_example_1():
    """
    Generate main body of a tikz code for a spanning tree (example 1).
    """
    tikz_code = build_body_of_tikz_spanning_tree(
        num_of_servers=1, threshold=2, system_capacity=3, buffer_capacity=4
    )
    assert isinstance(tikz_code, str)
    assert (
        tikz_code
        == "\n\n\\begin{tikzpicture}[-, node distance = 1cm, auto]\n\\node[state] (u0v0) {(0,0)};\n\\node[state, right=of u0v0] (u0v1) {(0,1)};\n\\draw[->](u0v1) edge node {\\(1\\mu \\)} (u0v0);\n\\node[state, right=of u0v1] (u0v2) {(0,2)};\n\\draw[->](u0v2) edge node {\\(1\\mu \\)} (u0v1);\n\\node[state, below=of u0v2] (u1v2) {(1,2)};\n\\draw[->](u1v2) edge node {\\(1\\mu \\)} (u0v2);\n\\node[state, below=of u1v2] (u2v2) {(2,2)};\n\\draw[->](u2v2) edge node {\\(1\\mu \\)} (u1v2);\n\\node[state, below=of u2v2] (u3v2) {(3,2)};\n\\draw[->](u3v2) edge node {\\(1\\mu \\)} (u2v2);\n\\node[state, below=of u3v2] (u4v2) {(4,2)};\n\\draw[->](u4v2) edge node {\\(1\\mu \\)} (u3v2);\n\\node[state, right=of u0v2] (u0v3) {(0,3)};\n\\node[state, right=of u1v2] (u1v3) {(1,3)};\n\\node[state, right=of u2v2] (u2v3) {(2,3)};\n\\node[state, right=of u3v2] (u3v3) {(3,3)};\n\\node[state, right=of u4v2] (u4v3) {(4,3)};\n\\draw[->](u4v3) edge node {\\(1\\mu \\)} (u4v2);\n"
    )


def test_build_body_of_tikz_spanning_tree_example_2():
    """
    Generate main body of a tikz code for a spanning tree (example 2).
    """
    tikz_code = build_body_of_tikz_spanning_tree(
        num_of_servers=3, threshold=1, system_capacity=3, buffer_capacity=3
    )
    assert isinstance(tikz_code, str)
    assert (
        tikz_code
        == "\n\n\\begin{tikzpicture}[-, node distance = 1cm, auto]\n\\node[state] (u0v0) {(0,0)};\n\\node[state, right=of u0v0] (u0v1) {(0,1)};\n\\draw[->](u0v1) edge node {\\(1\\mu \\)} (u0v0);\n\\node[state, below=of u0v1] (u1v1) {(1,1)};\n\\draw[->](u1v1) edge node {\\(1\\mu \\)} (u0v1);\n\\node[state, below=of u1v1] (u2v1) {(2,1)};\n\\draw[->](u2v1) edge node {\\(1\\mu \\)} (u1v1);\n\\node[state, below=of u2v1] (u3v1) {(3,1)};\n\\draw[->](u3v1) edge node {\\(1\\mu \\)} (u2v1);\n\\node[state, right=of u0v1] (u0v2) {(0,2)};\n\\node[state, right=of u1v1] (u1v2) {(1,2)};\n\\node[state, right=of u2v1] (u2v2) {(2,2)};\n\\node[state, right=of u3v1] (u3v2) {(3,2)};\n\\draw[->](u3v2) edge node {\\(2\\mu \\)} (u3v1);\n\\node[state, right=of u0v2] (u0v3) {(0,3)};\n\\node[state, right=of u1v2] (u1v3) {(1,3)};\n\\node[state, right=of u2v2] (u2v3) {(2,3)};\n\\node[state, right=of u3v2] (u3v3) {(3,3)};\n\\draw[->](u3v3) edge node {\\(3\\mu \\)} (u3v2);\n"
    )


def test_get_tikz_code_for_permutation_example_1():
    """
    Generate tikz code for a specific permutation (example 1).
    """
    array = ["D", "D", "D", "D", "D"]
    assert (
        get_tikz_code_for_permutation(
            edges=array,
            num_of_servers=2,
            threshold=3,
            system_capacity=8,
            buffer_capacity=1,
        )
        == "\\draw[->](u0v4) edge node {\\(\\lambda_2 \\)} (u1v4);\n\\draw[->](u0v5) edge node {\\(\\lambda_2 \\)} (u1v5);\n\\draw[->](u0v6) edge node {\\(\\lambda_2 \\)} (u1v6);\n\\draw[->](u0v7) edge node {\\(\\lambda_2 \\)} (u1v7);\n\\draw[->](u0v8) edge node {\\(\\lambda_2 \\)} (u1v8);\n"
    )


def test_get_tikz_code_for_permutation_example_2():
    """
    Generate tikz code for a specific permutation (example 2).
    """
    array = ["D", "L", "D", "L", "D"]
    assert (
        get_tikz_code_for_permutation(
            edges=array,
            num_of_servers=2,
            threshold=3,
            system_capacity=8,
            buffer_capacity=1,
        )
        == "\\draw[->](u0v4) edge node {\\(\\lambda_2 \\)} (u1v4);\n\\draw[->](u0v5) edge node {\\(2\\mu \\)} (u0v4);\n\\draw[->](u0v6) edge node {\\(\\lambda_2 \\)} (u1v6);\n\\draw[->](u0v7) edge node {\\(2\\mu \\)} (u0v6);\n\\draw[->](u0v8) edge node {\\(\\lambda_2 \\)} (u1v8);\n"
    )


def test_get_tikz_code_for_permutation_example_3():
    """
    Generate tikz code for a specific permutation (example 3).
    """
    array = ["R", "D", "R", "D", "L", "L"]
    assert (
        get_tikz_code_for_permutation(
            edges=array,
            num_of_servers=3,
            threshold=3,
            system_capacity=5,
            buffer_capacity=3,
        )
        == "\\draw[->](u0v4) edge node {\\(\\lambda_1 \\)} (u0v5);\n\\draw[->](u0v5) edge node {\\(\\lambda_2 \\)} (u1v5);\n\\draw[->](u1v4) edge node {\\(\\lambda_1 \\)} (u1v5);\n\\draw[->](u1v5) edge node {\\(\\lambda_2 \\)} (u2v5);\n\\draw[->](u2v4) edge node {\\(3\\mu \\)} (u2v3);\n\\draw[->](u2v5) edge node {\\(3\\mu \\)} (u2v4);\n"
    )


def test_generate_code_for_tikz_spanning_trees_rooted_at_00_example_1():
    """
    Test that a given example of a Markov chain model (1121) returns the correct
    tikz code for two spanning trees
    """
    latex_code = list(generate_code_for_tikz_spanning_trees_rooted_at_00(1, 1, 2, 1))

    assert (
        latex_code[0]
        == "\n\n\\begin{tikzpicture}[-, node distance = 1cm, auto]\n\\node[state] (u0v0) {(0,0)};\n\\node[state, right=of u0v0] (u0v1) {(0,1)};\n\\draw[->](u0v1) edge node {\\(\\mu \\)} (u0v0);\n\\node[state, below=of u0v1] (u1v1) {(1,1)};\n\\draw[->](u1v1) edge node {\\(\\mu \\)} (u0v1);\n\\node[state, right=of u0v1] (u0v2) {(0,2)};\n\\node[state, right=of u1v1] (u1v2) {(1,2)};\n\\draw[->](u1v2) edge node {\\(\\mu \\)} (u1v1);\n\\draw[->](u0v2) edge node {\\(\\lambda_2 \\)} (u1v2);\n\\end{tikzpicture}"
    )

    assert (
        latex_code[1]
        == "\n\n\\begin{tikzpicture}[-, node distance = 1cm, auto]\n\\node[state] (u0v0) {(0,0)};\n\\node[state, right=of u0v0] (u0v1) {(0,1)};\n\\draw[->](u0v1) edge node {\\(\\mu \\)} (u0v0);\n\\node[state, below=of u0v1] (u1v1) {(1,1)};\n\\draw[->](u1v1) edge node {\\(\\mu \\)} (u0v1);\n\\node[state, right=of u0v1] (u0v2) {(0,2)};\n\\node[state, right=of u1v1] (u1v2) {(1,2)};\n\\draw[->](u1v2) edge node {\\(\\mu \\)} (u1v1);\n\\draw[->](u0v2) edge node {\\(\\mu \\)} (u0v1);\n\\end{tikzpicture}"
    )


def test_generate_code_for_tikz_spanning_trees_rooted_at_00_example_2():
    """
    Test that for a fixed buffer_capacity (here is set to 2) and a fixed difference
    between the system_capacity and the threshold, the number of spanning trees
    generated remain the same (here is 169 = 13^2 because buffer capacity is set to 2)
    """
    num_of_trees = 169
    for system_capacity in range(4, 7):
        latex_code = list(
            generate_code_for_tikz_spanning_trees_rooted_at_00(
                num_of_servers=1,
                threshold=system_capacity - 3,
                system_capacity=system_capacity,
                buffer_capacity=2,
            )
        )
        assert len(latex_code) == num_of_trees


def test_generate_code_for_tikz_spanning_trees_rooted_at_00_example_3():
    """
    Test that for a fixed threshold (set to 1) the number of spanning trees when
    altering the system capacity and buffer capacity is correct.

    Note that:
        number_of_trees = (number_of_trees when buffer_capacity is 1) ^ buffer_capacity
    """
    num_of_trees = [2, 5, 13, 34, 89]
    for system_capacity in range(2, 5):
        for buffer_capacity in range(1, 3):
            latex_code = list(
                generate_code_for_tikz_spanning_trees_rooted_at_00(
                    num_of_servers=1,
                    threshold=1,
                    system_capacity=system_capacity,
                    buffer_capacity=buffer_capacity,
                )
            )
            assert (
                len(latex_code) == num_of_trees[system_capacity - 2] ** buffer_capacity
            )
