#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'seanwa'

#import logging
#import os
#import sys
#import time
#import copy

from collections import Counter

'''
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
'''

# used to store each counter
score = 0
flag = False
#result_list = [0 for i in range(100)]

# combine the continue same type jewel
def combine_jewel():
	global jewel_list, score, flag
	c_flag = False
	tmp_count = 0
	
	if len(jewel_list) == 0:
		print score
		return
	if flag:
		# no continue items
		tmp = Counter(jewel_list).most_common()[-1]
		for i in range(0, len(jewel_list)):
			for j in range(0, tmp[1]):
				if jewel_list[i] == tmp[0]:
					jewel_list.remove(jewel_list[i])
					tmp_count += 1
				else:
					break
			if tmp_count > 0:
				score += (tmp_count * tmp_count)
				tmp_count = 0
				flag = False
				break
	else:
		# exist continue items
		for i in range(0, len(jewel_list)):
			num = jewel_list.count(jewel_list[i])
			if cmp(jewel_list[i:i+num], [jewel_list[i]]*num) == 0:
				c_flag = True
				for j in range(0, num):
					jewel_list.remove(jewel_list[i])
					tmp_count += 1
				break
		if c_flag:
			flag = False
		else:
			flag = True
		score += (tmp_count * tmp_count)
		c_flag = False
		tmp_count = 0
	
	combine_jewel()

# main function
jewel_list = raw_input().split(",")
#tmp_jewel_list = copy.deepcopy(jewel_list)
#list_num = Counter(tmp_jewel_list).most_common()

combine_jewel()
'''
for index in range(0, len(list_num)):
	print list_num[index]
	jewel_list = copy.deepcopy(tmp_jewel_list)
	combine_jewel(index)
'''