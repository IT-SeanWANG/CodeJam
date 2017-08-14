#!/usr/bin/python
# -*- coding: UTF-8 -*-
matrix = [[0 for i in range(9)] for i in range(9)];
for i in range(0,9):
	box = raw_input().split(',');
	for j in range(0,9):
		matrix[i][j] = int(box[j]);
rt = range(1,10);
for i in range(0,9):
	row = [0 for k in range(9)];
	row = matrix[i][:];
	row.sort();
	if(rt!=row):
		print -1;
		exit(0);
for i in range(0,9):
	col = [0 for k in range(9)];
	for j in range(0,9):
		col[j] = matrix[j][i];
	col.sort();
	if(rt!=col):
		print -1;
		exit(0);
x = y = [[0,1,2],[3,4,5],[6,7,8]];
for xi in x:
	for yi in y:
		count = 0;
		rc = [0 for k in range(9)];
		for m in xi:
			for n in yi:
				rc[count] = matrix[m][n];
				count +=1;
		rc.sort();
		if(rt!=rc):
			print -1;
			exit(0);
print 1;

	
