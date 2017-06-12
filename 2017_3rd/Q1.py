#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'seanwa'

# main function
length = 0
version_list = raw_input().split(" ")
version_1 = version_list[0].split(".")
version_2 = version_list[1].split(".")
if len(version_1) > len(version_2):
	length = len(version_1)
	for i in range(len(version_2), len(version_1)):
		version_2.append(0)
elif len(version_2) > len(version_1):
	length = len(version_2)
	for i in range(len(version_1), len(version_2)):
		version_1.append(0)
else:
	length = len(version_1)

for i in range(0, length):
	if int(version_1[i]) > int(version_2[i]):
		print 1
		exit()
	elif int(version_1[i]) < int(version_2[i]):
		print -1
		exit()
	else:
		continue
print 0
