#!/usr/bin/python3
"""
Python Pascal Triangle
"""


def pascal_triangle(n):
    """creating the triangle"""

    res = []
    if n <= 0:
        return res
    for i in range(n):
        tempList = []

        for j in range(i + 1):
            if j == 0 or j == i:
                tempList.append(1)
            else:
                tempList.append(res[i - 1][j - 1] + res[i - 1][j])
        res.append(tempList)
    return res
