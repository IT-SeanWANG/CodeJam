#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'Sean WANG'

import os
import sys
import time
import copy

MAX_TIME = 1000000000
MAX_PRO = 10000

# convert the input
def strtolist(str):
    start_time = int(str.split()[0])
    end_time = int(str.split()[1])
    return [start_time, end_time]

# check input valid
def inputisvalid(in_num, max_limit):
    if in_num <= max_limit:
        return True
    else:
        return False


# filter process as time range
def filter_process_list(process_list, time_range):
    tmp_list = copy.copy(process_list)
    for item in process_list:
        if item[0] > time_range[1] or item[1] < time_range[0]:
            tmp_list.remove(item)
    return tmp_list


# get time point when there are process open or close
def filter_time_point(process_list, time_range):
    tmp_list = []
    for item in process_list:
        if item[0] >= time_range[0]:
            tmp_list.append([item[0], 1])
        if item[1] <= time_range[1]:
            tmp_list.append([item[1], -1])
    tmp_list.sort()
    return tmp_list


# read input
valid_flg = 0
time_range = []
process_nb = 0
g_process_tlist = []
# read valid input time range
while 0 == valid_flg:
    str = raw_input()
    tmp_str = str.split()
    if len(tmp_str) != 2:
        print 'Invalid input, please input time range again'
        continue
    time_range = strtolist(str)
    if 0 <= time_range[0] <= time_range[1] and inputisvalid(time_range[1], MAX_TIME):
        valid_flg = 1
    else:
        print 'Invalid input, please input time range again'

# read valid input process nb
valid_flg = 0
while 0 == valid_flg:
    str = raw_input()
    tmp_str = str.split()
    if len(tmp_str) != 1:
        print 'Invalid input, please input process number again'
        continue
    process_nb = int(str)
    if inputisvalid(process_nb, MAX_PRO):
        valid_flg = 1
    else:
        print 'Invalid input, please input process number again'

# read valid input process time range
for i in range(0, process_nb):
    valid_flg = 0
    while 0 == valid_flg:
        str = raw_input()
        tmp_str = str.split()
        if len(tmp_str) != 2:
            print 'Invalid input, please input %s th process time range again' % (i + 1)
            continue
        l_time_range = strtolist(str)
        if 0 <= l_time_range[0] <= l_time_range[1] and inputisvalid(l_time_range[1], MAX_TIME):
            valid_flg = 1
        else:
            print 'Invalid input, please input %s th process time range again' % (i + 1)
    g_process_tlist.append(l_time_range)

# begin to compute max and min process number
g_process_tlist = filter_process_list(g_process_tlist, time_range)
time_point_list = filter_time_point(g_process_tlist, time_range)

# process nb == 0 ==> max = min = 0
if 0 == len(g_process_tlist):
    print 0
    print 0
    exit()

# to record process nb of every time point when process nb change
count_list = []
count = 0
begin_value = 0
# make sure the start value of the point that time range begin
for pro_item in g_process_tlist:
    if pro_item[1] >= time_range[0] > pro_item[0]:
        count += 1
begin_value = count

tmp_value = time_point_list[0][0]
if time_range[0] != tmp_value:
    count_list.append(begin_value)

# algorithm : record process num as time line - add when open or minus when close
count_all = 0
count_add = 0
for item in time_point_list:
    if tmp_value != item[0]:
        tmp_value = item[0]
        count_list.append(begin_value + count_add)
        count_list.append(begin_value + count_all)
        begin_value += count_all
        count_all = 0
        count_add = 0
        count_all += item[1]
        if 1 == item[1]:
            count_add += 1
    else:
        count_all += item[1]
        if 1 == item[1]:
            count_add += 1

count_list.append(begin_value + count_add)

if time_point_list[-1][0] != time_range[1]:
    count_list.append(begin_value + count_all)

# output
print min(count_list)
print max(count_list)
