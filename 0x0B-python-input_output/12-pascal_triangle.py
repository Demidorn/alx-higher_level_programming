#!/usr/bin/python3
"""
pascal triangle
return lists of lists of integers

"""


def pascal_triangle(n):
    """
    return list of lists of int
    """
    tri_list = [[]]
    if n <= 0:
        return tri_list
    for j in range(1, n + 1):
        tri_list.append([])
        for ele in range(li):
            if ele == 0 or ele == j - 1:
                tri_list[j].append(1)
            else:
                tri_list[j].append(tri_list[j-1][ele] + tri_list[j-1][ele-1])

    return tri_list[1:]
