#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'Sean'


# main function
child_num, start, step = map(int, raw_input().split(' '))
child_list = []
for i in range(child_num + 1):
	child_list.append(i)
result_list = [0 for i in range(child_num+1)]
new_start = 0
left_num = child_num
tmp_step = 0
init_flag = True
while(left_num > 2):
	tmp_step = step%left_num
	if init_flag and tmp_step == 0:
		tmp_step = 1
	if tmp_step + child_list.index(start) <= left_num:
		new_start = child_list.index(start) + tmp_step
	else:
		new_start = child_list.index(start) + tmp_step - left_num
	
	if not init_flag:
		if new_start != 1:
			new_start -= 1
		else:
			new_start = left_num
	else:
		init_flag = False
	
	index = new_start
	if index < left_num:
		index += 1
		start = child_list[index]
	else:
		start = child_list[1]
	child_list.remove(child_list[new_start])
	left_num -= 1
print child_list[1],child_list[2]

'''
约瑟夫环问题
Appendix test case
#test 1: 2 3
3 2 2

#test 2: 2 4
4 3 2

#test 3: 2 5
5 3 3
'''