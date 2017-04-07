#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'seanwa'

import logging

import os
import sys
import time
import copy

# log config
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='py.log',
                    filemode='w')

logging.error('This is error message')
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

MIN_NUM = 2
MAX_NUM = 10
MIN_NUM_CANDY = 1
MAX_NUM_CANDY = 50
# used to store 0~9A~Za~z
result_list = [0 for i in range(62)]


# check input children number valid
def valid_num(num):
    if MIN_NUM <= num <= MAX_NUM:
        return True
    else:
        return False


# convert input ASCII to number
def covert_alpha2num(ascii):
    i = 0
    # convert to number
    num = ord(ascii)
    logging.info('start to covert alpha[%d] to number', num)
    # 0~9
    if 48 <= num <= 57:
        i = num - 48
    # A~Z
    elif 65 <= num <= 90:
        i = num - 55
    # a~z
    elif 97 <= num <= 122:
        i = num - 61
    else:
        logging.error('input a wrong alpha')
        return False

    result_list[i] += 1
    logging.info('result_list[%d] is %d', i, result_list[i])
    return True


# check input candy format and sort
def valid_sort_candy(str_candy):
    box_num = 0
    candy_num = 0

    # min input should be "x"
    str_len = len(str_candy)
    logging.info('input string length is %d', str_len)
    if str_len < 3:
        logging.error('input invalid')
        return False

    # deal the first and the last input
    if cmp(str_candy[0], "\"") or cmp(str_candy[-1], "\""):
        logging.error('input invalid')
        return False
    if str_candy[1] == "," or str_candy[-2] == ",":
        logging.error('input invalid')
        return False

    # verify the box and number limit 1~50
    list_tmp = "".join(str_candy.split("\"")).split(",")
    if len(list_tmp) > MAX_NUM_CANDY:
        logging.error('input invalid')
        return False
    for i in range(0, len(list_tmp)):
        if len(list_tmp[i]) > MAX_NUM_CANDY:
            logging.error('input invalid')
            return False

    # deal other input info
    for index in range(1, str_len - 1):
        if str_candy[index-1] == str_candy[index] == "\"" or str_candy[index] == str_candy[index+1] == "\"":
            logging.error('input invalid')
            return False
        if str_candy[index] == "," and (str_candy[index-1] != "\"") and (str_candy[index+1] != "\""):
            logging.error('input invalid')
            return False

        # deal each character
        if str_candy[index] == "\"" or str_candy[index] == ",":
            logging.info('current string is %s', str_candy[index])
            continue
        elif covert_alpha2num(str_candy[index]):
            continue
        else:
            return False

    return True


# main function
children_num = 0
give_num = 0
left_num = 0
str_num = raw_input()
if str_num.isdigit():
    if not valid_num(int(str_num)):
        logging.error('invalid result')
        print '-1,-1'
        exit(-1)
    children_num = int(str_num)
else:
    logging.error('invalid result')
    print '-1,-1'
    exit(-1)

if not valid_sort_candy(raw_input()):
    logging.error('invalid result')
    print '-1,-1'
    exit(-1)
for i in range(0, 62):
    give_num += result_list[i]//children_num
    left_num += result_list[i]%children_num
print "%d,%d"%(give_num, left_num)
