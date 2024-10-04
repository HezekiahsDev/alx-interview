#!/usr/bin/python3

"""
Create Pascal Triangle
"""


def fact(n):
    """
    n factorial
    """
    if n < 0:
        return None  # or raise an exception
    elif n == 0:
        return 1
    else:
        return n * fact(n - 1)


def pascal_triangle(n):
    """
    Create the pascal triangle of n
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(fact(i) // (fact(j) * fact(i - j)))
        triangle.append(row)
    return triangle
