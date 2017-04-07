#! /usr/bin/env python
# coding: utf-8
# python version: python 27

import os
import sys
import time
import numpy as np
import logging

logging.basicConfig(format='[%(levelname)s]:%(asctime)s:%(filename)s:%(lineno)d:%(message)s',
                    datefmt='%Y:%m:%d-%H:%M:%S', level=logging.ERROR)

logging.debug("this is the begining of Q1")

MIN = 1
MAX = 250
COR_MAX = pow(10, 7)

list_man = [[0, 1], [0, 2], [0, 3]]
list_car = [[100, 1], [200, 2], [300, 3]]

# function to compute time man --> car
def compute_time(cor_man, cor_car):
    tmp_time = 0
    tmp_time = abs(cor_man[0] - cor_car[0]) + abs(cor_man[1] - cor_car[1])
    return tmp_time

# get a matrix to express all time man --> car
# [[100, 201, 302],
#  [101, 200, 301],
#  [102, 201, 300]]
def get_time_matrix(l_list_man, l_list_car):
    time_matrix = []
    for item_man in l_list_man:
        man_matrix = []
        for item_car in l_list_car:
            man_matrix.append(compute_time(item_man, item_car))
        time_matrix.append(man_matrix)
    return time_matrix


def getPositon(l_matrix):
    a = np.mat(l_matrix)
    raw, column = a.shape  # get the matrix of a raw and column
    _positon = np.argmax(a)  # get the index of min in the a
    # print _positon
    m, n = divmod(_positon, column)
    logging.debug( "The raw is %s", m)
    logging.debug("The column is %s", n)
    logging.debug("The max of the a is %s", a[m, n])
    return a[m,n], m, n

# remove a raw of a matrix
def remove_raw(l_matrix):
    for i, item in enumerate(l_matrix):
        if [-1] == list(set(item)):
            l_matrix.pop(i)
    return l_matrix

# remove a column of a matrix
def remove_column(l_matrix):
    len_col = l_matrix[0].__len__()
    for i in range(0, len_col):
        tmp_list = [x[i] for x in l_matrix]
        if [-1] == list(set(tmp_list)):
            for l_item in l_matrix:
                l_item.pop(i)
            break
    return l_matrix

# remove ram and column of a matrix
# l_matrix, raw, column
def remove_matrix(l_matrix, m, n):
    l_matrix[m][n] = -1
    l_matrix = remove_raw(l_matrix)
    l_matrix = remove_column(l_matrix)
    return l_matrix
# print compute_time(list_man[0], list_car[2])

# tmp_matrix = [[101, 100, 302],[101, 100, 301],[102, 201, 300]]
# getPositon(tmp_matrix)

# get the order to board the car
def get_order(l_time_matrix, k):
    board_car_list = []
    tmp_matrix = l_time_matrix
    # for i in range(0, k):
    while True:
        position = getPositon(tmp_matrix)
        board_car_list.append(position[0])
        tmp_matrix = remove_matrix(tmp_matrix, position[1], position[2])

        if tmp_matrix.__len__() < k:
            # print board_car_list,tmp_matrix
            return board_car_list
        if tmp_matrix[0].__len__() < k:
            # print board_car_list,tmp_matrix
            return board_car_list

# get result used in main function
# result_time = np.int64(0)

def get_result(man_list, car_list, k):
    l_time_matrix = get_time_matrix(man_list, car_list)
    logging.debug("The l_time_matrix is %s", l_time_matrix)
    board_time_list = get_order(l_time_matrix, k)
    logging.info("The board_time_list is %s", board_time_list[-1])
    # result_time = pow(board_time_list[-1],2)
    tmp = np.longlong(board_time_list[-1])
    result_time = pow(tmp, 2)
    # result_time = board_time_list[-1] * board_time_list[-1]
    logging.info("The result_time is %s", result_time)
    return result_time

# tmp_matrix = get_time_matrix(list_man, list_car)
# board_car_order = get_order(tmp_matrix,2)
# print board_car_order

# str to list
def str2list(l_str):
    tmp = l_str.split()
    if 0 != tmp.__len__() % 2:
        return -1
    result_list = []
    tmp_list = []
    i = 0

    for item in tmp:
        i = i + 1
        tmp_val = int(item)
        if not 0 <= tmp_val <= COR_MAX:
            return -1
        tmp_list.append(tmp_val)

        if i % 2 == 0:
            result_list.append(tmp_list)
            tmp_list = []

    return result_list

# print str2list("1 2 3 4 5 6")

# man function
def solution(N, M, K, NP, MP):
    if not MIN <= N <= MAX :
        return -1
    if not MIN <= M <= MAX :
        return -1
    if not MIN <= K <= min(M, N) :
        return -1
    m_list_man = str2list(NP)
    if -1 == m_list_man:
        return -1
    m_list_car = str2list(MP)
    if -1 == m_list_car:
        return -1
    print get_result(m_list_man, m_list_car, K)
    return 0

# solution(3,3,2,'0 1 0 2 0 3 ','100 1 200 2 300 3')
# solution(3, 3, 3,'0 1 0 1 0 1','100 1 100 1 100 1')
# solution(4, 4, 3,'0 1 0 1 0 1 0 1','100 1 200 1 300 1 400 1')
# solution(4, 2 ,2,'0 1 1 1 2 1 3 1','100 1 200 1')
# solution(2 ,4, 2, '0 1 1 1','100 1 200 1 300 1 400 1')
# solution(2, 4, 2,'0 1 1 1','100 1 100 1 100 1 100 1')
# solution(2, 4, 2,'0 1 0 1','100 1 200 1 300 1 400 1')

#  read input
def read_input():
    str = raw_input()
    tmp_str = str.split()
    nb_man = int(tmp_str[0])
    if not MIN <= nb_man <= MAX :
        return -1
    nb_car = int(tmp_str[1])
    if not MIN <= nb_car <= MAX :
        return -1
    k = int(tmp_str[2])
    if not MIN <= k <= min(nb_man, nb_car) :
        return -1

    np = nb_man
    man_str = ''
    while np:
        # print "pls input man lo"
        str2 = raw_input()
        tmp_str = str2.split()
        # print tmp_str
        if not 0 <= int(tmp_str[0])<= COR_MAX:
            return -1
        if not 0 <= int(tmp_str[1]) <= COR_MAX:
            return -1
        man_str += str2
        man_str += ' '
        np = np -1
        # print man_str

    nc = nb_car
    car_str = ''
    while nc:
        # print nc
        str2 = raw_input()
        tmp_str = str2.split()
        if not 0 <= int(tmp_str[0]) <= COR_MAX:
            return -1
        if not 0 <= int(tmp_str[1]) <= COR_MAX:
            return -1
        car_str += str2
        car_str += ' '
        nc = nc - 1

    solution(nb_man, nb_car, k, man_str, car_str)






read_input()