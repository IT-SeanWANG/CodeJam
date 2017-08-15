#!/usr/bin/python
# -*- coding: UTF-8 -*-
lr = raw_input().split();
lab = int(lr[0]);
robert = int(lr[1]);
rc = raw_input().split();
for i in range(len(rc)):
	rc[i] = int(rc[i]);

ls = 0;

maxY = max(rc);
lc = [];
for i in range(1,maxY):
	num = 0;
	for j in range(robert):
		num += rc[j]/i;
	if(num>=lab):
		ls = i;
	else:
		ls = i-1;
		break;
for i in range(robert):
	lc.append(rc[i]/ls);

box = [[sum(rc) for i in range(lab+1)] for i in range(len(lc))];
for i in range(len(lc)):
	box[i][0] = 0;
for i in range(len(lc)):
	for j in range(1,(lab+1)):
		box[i][j] = min(box[i-1][j],box[i-1][j-lc[i]]+rc[i]);

print ls,box[len(lc)-1][lab];