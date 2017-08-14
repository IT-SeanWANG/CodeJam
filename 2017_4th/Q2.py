#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'Sean'

# variables
dish_price = [0 for i in range(10)]
count = 0
sum = 0
'''
result = [0 for i in range(500)]
top = 0
'''

# deep-first-search to calculate the possible combine
def dfs_combine(index):
	global count, sum
	#global result, top
	
	if sum == meal_ticket:
		count += 1
		'''
		print "%s=" %sum
		for k in range(top):
			print "%s+" %result[k]
		'''
		return
	elif sum > meal_ticket:
		return
	for i in range(index, len(dish_price)):
		#result[top] = int(dish_price[i])
		#top += 1
		sum += int(dish_price[i])
		dfs_combine(i)
		sum -= int(dish_price[i])
		#top -= 1

# main function
# meal_ticket range 1-500; dish_price range 1-10
meal_ticket = int(raw_input())
dish_price = raw_input().split(",")
dfs_combine(0)
print count