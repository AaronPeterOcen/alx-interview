#!/usr/bin/python3
"""
Python Pascal Triangle
"""


def pascal_triangle(n):
    """creating the triangle"""

    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []

            a = 1
            for j in range(1, i + 1):
                level.append(a)
                a = a * (i - j)
            res.append(level)

    return res
