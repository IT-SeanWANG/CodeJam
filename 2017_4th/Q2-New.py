#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'Sean'

# variables
count = 0

# dynamic-search to solve integer divide issue
def dynamic_combine():
	global count
	for i in range(0, len(dish_list)):
		if i == 0:
			for j in range(0, len(dish_price)):
				dish_list[i][j] = 0
		else:
			for j in range(0, len(dish_price)):
				if int(dish_price[j]) == 1:
					dish_list[i][j] = 1
				else:
					if i < int(dish_price[j]):
						dish_list[i][j] = dish_list[i][j-1]
					elif i == int(dish_price[j]):
						dish_list[i][j] = dish_list[i][j-1] + 1
					elif i > int(dish_price[j]):
						dish_list[i][j] = dish_list[i - int(dish_price[j])][j] + dish_list[i][j-1]
	count = dish_list[meal_ticket][len(dish_price) - 1]

# main function
# meal_ticket range 1-500; dish_price range 1-10
meal_ticket = int(raw_input())
dish_price = raw_input().split(",")
dish_list = [[0 for col in range(len(dish_price))]for row in range(meal_ticket+1)]
dynamic_combine()
print count