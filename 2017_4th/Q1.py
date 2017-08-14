#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'Sean'


# @param sudoku 9x9 array
# @return a boolean
def is_valid_sudoku(sudoku):
	rows = [list(lst[::]) for lst in sudoku]
	columns = [[lst[idx] for lst in sudoku] for idx in range(9)]
	blocks_origin = [sudoku[row][column] for x in [[0, 1, 2], [3, 4, 5], [6, 7, 8]] for y in [[0, 1, 2], [3, 4, 5], [6, 7, 8]] for row in x for column in y]
	# convert to list
	blocks = [[blocks_origin[row * 9 + column] for column in range(9)] for row in range(9)]
	# for only several numbers is put in case '.' means no number is set in this position
	#check = lambda lst: all([lst.count(x) == 1 for x in lst if x != '.'])
	# make sure one element in rows, columns  and blocks are only
	check = lambda lst: all([lst.count(x) == 1 for x in lst])
	return all([check(x) for style in (rows, columns, blocks) for x in style])

# main function
# initial 9x9 array
sudoku_list = [[0 for col in range(9)]for row in range(9)]
for i in range(9):
	sudoku_list[i] = raw_input().split(",")

if(is_valid_sudoku(sudoku_list)):
	print 1
else:
	print -1

'''
Appendix test case
#test 1: True
5, 3, 4, 6, 7, 8, 9, 1, 2
6, 7, 2, 1, 9, 5, 3, 4, 8
1, 9, 8, 3, 4, 2, 5, 6, 7
8, 5, 9, 7, 6, 1, 4, 2, 3
4, 2, 6, 8, 5, 3, 7, 9, 1
7, 1, 3, 9, 2, 4, 8, 5, 6
9, 6, 1, 5, 3, 7, 2, 8, 4
2, 8, 7, 4, 1, 9, 6, 3, 5
3, 4, 5, 2, 8, 6, 1, 7, 9
#test 2: True
4, 8, 3, 2, 7, 1, 6, 9, 5
9, 7, 6, 4, 8, 5, 3, 2, 1
5, 2, 1, 3, 9, 6, 4, 7, 8
2, 9, 4, 6, 5, 8, 1, 3, 7
1, 3, 8, 9, 2, 7, 5, 6, 4
6, 5, 7, 1, 3, 4, 9, 8, 2
8, 4, 2, 5, 6, 3, 7, 1, 9
3, 1, 9, 7, 4, 2, 8, 5, 6
7, 6, 5, 8, 1, 9, 2, 4, 3
#test 3: False
1, 3, 2, 5, 7, 9, 4, 6, 8
4, 9, 8, 2, 6, 1, 3, 7, 5
7, 5, 6, 3, 8, 4, 2, 1, 9
6, 4, 3, 1, 5, 8, 7, 9, 2
5, 2, 1, 7, 9, 3, 8, 4, 6
9, 8, 7, 4, 2, 6, 5, 3, 1
2, 1, 4, 9, 3, 5, 6, 8, 7
3, 6, 5, 8, 1, 7, 9, 2, 4
8, 7, 9, 6, 4, 2, 1, 3, 5
#test 4: True
8, 1, 3, 9, 6, 5, 2, 7, 4
4, 5, 6, 8, 7, 2, 1, 9, 3
9, 7, 2, 1, 3, 4, 6, 8, 5
3, 6, 5, 4, 9, 1, 7, 2, 8
2, 9, 4, 7, 5, 8, 3, 1, 6
7, 8, 1, 3, 2, 6, 4, 5, 9
1, 4, 7, 5, 8, 3, 9, 6, 2
5, 2, 9, 6, 4, 7, 8, 3, 1
6, 3, 8, 2, 1, 9, 5, 4, 7
'''