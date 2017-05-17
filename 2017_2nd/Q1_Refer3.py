#!/usr/bin/python
# -*- coding: UTF-8 -*-
total_num = int(raw_input());
matrix = raw_input().split();
b=[];
for str in matrix:
	b.append(int(str));
flag = [0]*total_num;

bg = b[0];
pos = 0;
count = 0;

for i in range(total_num):
	for j in range(total_num-i-1):
		if(abs(b[j])>abs(b[j+1])):
			temp = b[j];
			b[j] = b[j+1];
			b[j+1] = temp;
			if(pos==j):
				pos = (j+1);

flag[pos]=1;
while(1):
	change = 0;
	for i in range(total_num-1):
		if(b[i]>0 and b[i+1]<0):
			b[i]=0-b[i];
			b[i+1]=0-b[i+1];
			if(flag[i] or flag[i+1]):
				flag[i]=flag[i+1]=1;
			change = 1;
	if(change==0):
		break;
for i in range(total_num):
	if(flag[i]):
		count = count+1;
print count;
