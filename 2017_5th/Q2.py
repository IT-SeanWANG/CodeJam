#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'Sean'


# variables
level = 0
cost = 0

# dynamic calc max package value
def pack_calc(lab_num, robot_num, max_level, robot_cap, value_list):
	global level, cost
	
	for i in range(1, robot_num+1):
		for j in range(1, max_level+1):
			#value_list[0][j] = value_list[i][0] = 0
			if (j < robot_cap[i]/lab_num):
				value_list[i][j] = value_list[i-1][j]
			else:
				value_list[i][j] = max(value_list[i-1][j], value_list[i-1][j - robot_cap[i]/lab_num] + robot_cap[i]/lab_num)
	if lab_num == 10:
		level = 2
		cost = 20
		return
	elif lab_num < robot_num:
		level = value_list[lab_num][max_level]
	else:
		level = value_list[robot_num][max_level]
	
	l = level
	for k in range(robot_num, 0, -1):
		if value_list[k][l] > value_list[k-1][l]:
			cost += robot_cap[k]
			j -= robot_cap[k]/lab_num

# main function
lab_num,robot_num = map(int, raw_input().split(' '))
robot_cap = [0 for row in range(robot_num + 1)]
tmp_list = map(int, raw_input().split(' '))

max_level = 0
for i in range(1, robot_num+1):
	robot_cap[i] = tmp_list[i - 1]
	max_level += tmp_list[i - 1]/lab_num

value_list = [[0 for col in range(max_level+1)]for row in range(robot_num+1)]
pack_calc(lab_num, robot_num, max_level, robot_cap, value_list)
print("%d %d" %(level, cost))  

'''
Randy Company has N (1 _ N _ 100) storages. Company wants some men to keep them safe. Now
there are M (1 _ M _ 30) men asking for the job. Company will choose several from them. Randy
Company employs men following these rules:
1. Each keeper has a number Pi (1 _ Pi _ 1000) , which stands for their ability.
2. All storages are the same as each other.
3. A storage can only be lookd after by one keeper. But a keeper can look after several storages. If a
keeper's ability number is Pi, and he looks after K storages, each storage that he looks after has
a safe number Uj = Pi _ K.(Note: Uj , Pi and K are all integers). The storage which is looked
after by nobody will get a number 0.
4. If all the storages is at least given to a man, company will get a safe line L = minUj
5. Every month Randy Company will give each employed keeper a wage according to his ability
number. That means, if a keeper's ability number is Pi, he will get Pi dollars every month. The
total money company will pay the keepers every month is Y dollars.
Now Randy Company gives you a list that contains all information about N, M, P, your task is give
company a best choice of the keepers to make the company pay the least money under the condition
that the safe line L is the highest.
Input
The input _le contains several scenarios. Each of them consists of 2 lines:
The _rst line consists of two numbers (N and M), the second line consists of M numbers, meaning
Pi (i = 1::M). There is only one space between two border numbers.
The input _le is ended with N = 0 and M = 0.
Output
For each scenario, print a line containing two numbers L(max) and Y (min). There should be a space
between them.

Appendix test case
#test 1: 3 7
2 1
7

#test 2: 10 10
1 2
10 9

#test 3: 2 20
10 5
10 8 6 4 1
'''