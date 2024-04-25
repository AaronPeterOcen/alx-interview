#!/usr/bin/python3


def pascal_triangle(n):
    """creating the triangle"""

    if n <= 0:
        return []

    triangle = []

    triangle.append([1])

    for i in range(1, n):
        row = triangle[i - 1]
        row1 = [1]

        for j in range(1, i):
            row1.append(row[j - 1] + row[j])
            row1.append(1)
            triangle.append(row1)

    return triangle


print(pascal_triangle(5))
