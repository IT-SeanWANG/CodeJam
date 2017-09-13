#!/usr/bin/python
# -*- coding: UTF-8 -*-
nkm=raw_input().split();
n=int(nkm[0]);
k=int(nkm[1]);
m=int(nkm[2]);

def josephus(n,k,m):
	child_group=range(1,n+1);
	init_group=child_group[:];
	del init_group[k-1];
	begin_value = init_group[(k+m-1)%(n-1)-1];
	begin_child = child_group.index(begin_value);
	for i in range(n-2):
		del child_group[begin_child];
		begin_child = (begin_child+m-1)%len(child_group);
	print child_group[0],child_group[1];

josephus(n,k,m);