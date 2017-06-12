#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Compiled and executed in python 3.6

diamond_list = input().split(",")
diamond_total = len(diamond_list)
segment_color = [0 for i in range(diamond_total)]
segment_count = [0 for i in range(diamond_total)]
points = [[[0 for i in range(diamond_total)] for i in range(diamond_total)] for i in range(diamond_total)]
segment_color[0] = diamond_list[0]
segment_count[0] = 1
index = 0
for i in range(1, diamond_total):
    if diamond_list[i] == diamond_list[i - 1]:
        segment_count[index] += 1
    else:
        index += 1
        segment_color[index] = diamond_list[i]
        segment_count[index] = 1


def max_points(l, r, s):
    if(points[l][r][s] != 0):
        return points[l][r][s]
    if(l == r):
        points[l][r][s] = (s + segment_count[r]) ** 2
        return points[l][r][s]
    points[l][r][s] = max_points(l, r - 1, 0) + (s + segment_count[r])**2
    for i in range(l, r):
        if(segment_color[i] == segment_color[r]):
            points[l][r][s] = max(points[l][r][s], max_points(l, i, s + segment_count[r]) + max_points(i + 1, r - 1, 0))
    return points[l][r][s]

print(max_points(0, index, 0))
