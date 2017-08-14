#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'Sean'


# variables
num = 0

# @param x, y and node NxN array
# @return number of connect node
def num_connect_node(x, y, node_list):
	global n, v, num
	
	
	if (x < 0 or x >= n or y < 0 or y >= n or node_list[x][y] == 'F') or (v != node_list[x][y]):
		return 0
	num += 1
	node_list[x][y] = 'F'
	num_connect_node(x-1, y, node_list)
	num_connect_node(x+1, y, node_list)
	num_connect_node(x, y-1, node_list)
	num_connect_node(x, y+1, node_list)
	
	return num

# main function
x,y = map(int, raw_input().split(' '))
n = int(raw_input())
# initial NxN array
node_list = [[0 for col in range(n)]for row in range(n)]
for i in range(n):
	node_list[i] = raw_input().split(' ')
v = node_list[x][y]
print num_connect_node(x, y, node_list)


'''
Appendix test case
#test 1: 3
1 2
6
1 1 3 4 2 2
2 2 1 5 3 1
3 1 1 4 5 2
2 2 4 3 4 1
4 1 5 5 5 1
5 1 2 2 1 1

#test 2: 10
2 2
5
1 1 2 1 1
1 1 2 1 3
2 3 1 4 5
1 1 1 1 1
1 1 4 1 1

#test 3: 3
0 0
4
1 5 5 2
1 1 3 2
2 2 4 4
1 2 5 1
'''