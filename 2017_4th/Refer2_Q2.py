#!/usr/bin/python
# -*- coding: UTF-8 -*-
total = int(raw_input());
items = raw_input().split(',');
box = [[0 for i in range(len(items))] for j in range(total+1)];
for j in range(len(items)):
	items[j] = int(items[j]);
	box[0][j] = 0;
for i in range(1,total+1):
	for j in range(0,len(items)):
		if(i<items[j]):
			box[i][j] = box[i][j-1];
		elif(i==items[j]):
			box[i][j] = box[i][j-1] + 1;
		else:
			box[i][j] = box[i-items[j]][j] + box[i][j-1];
print box[total][len(items)-1];