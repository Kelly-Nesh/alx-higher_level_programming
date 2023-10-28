#!/usr/bin/python3
"""Module with a function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers."""
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print("{:d}".format(matrix[row][col]), end="")
            if col != len(matrix[row]) - 1:
                print(" ", end="")
        print()
