#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'Sean'


# variables
cases_num = 0
static_layer = 0
static_value = 0

'''
layer = 0
tmp_layer = 0

# recursion calc possible
def recursion_calc():
	global id, day, month, year, H, A, index, range, cases_num, layer, static_layer, static_value, tmp_layer
	
	if layer == 18:
		layer = static_layer
		tmp_layer = 0
		H = (H + static_value) % 19
		if H <= 9:
			calc_A = H
		else:
			calc_A = 19 - H
		if index[-1] != 18:
			if calc_A == A:
				cases_num += 1
		else:
			for i in range(10):
				if i == calc_A:
					cases_num += 1
					break
		return

	if len(index) > tmp_layer and index[tmp_layer] == tmp_layer:
		for j in range(v_range[tmp_layer]):
			if tmp_layer < 9:
				H += (10 - tmp_layer) * j
			else:
				H += (19 - tmp_layer) * j
			layer += 1
			tmp_layer += 1
			recursion_calc()
			return
'''

# main function
id = raw_input()
A = id[18]
'''
day = id[0:2]
print day
month = id[2:4]
print month
year = id[4:8]
print year
Z = id[8:18]
print Z
H = 0
'''

index = []
v_range = [1 for i in range(18)]
pos = 0

while (pos != -1 and pos != len(id)):
	#tmp_len = len(id[pos:])
	pos = id.find('B', pos, len(id))
	if (pos != -1):
		index.append(pos)
		pos += 1
# calc v_range
for i in range(len(index)):
	if index[i] == 0:
		#S1: 0~3
		v_range[index[i]] = 4
	elif index[i] == 2:
		#S3:0~1
		v_range[index[i]] = 2
	elif index[i] == 1 or index[i] == 3 or index[i] >= 4 and index[i] <= 17:
		#S2:0~9 need to exclude 00 case later
		#S4-S7:0~9 S8:1~9 need to exclude 0 case later S9-S18:0~9
		v_range[index[i]] = 10

for i in range(18):
	if id[i] != 'B':
		static_layer += 1
		if i < 9:
			static_value += (10 - i) * int(id[i])
		else:
			static_value += (19 - i) * int(id[i])
#layer = static_layer
#recursion_calc()

# since recursion can't pass debug, here just use the stupid method to calc
year = []
tmp_year = 0
for S1 in range(v_range[0]):
	for S2 in range(v_range[1]):
		for S3 in range(v_range[2]):
			for S4 in range(v_range[3]):
				for S5 in range(v_range[4]):
					for S6 in range(v_range[5]):
						for S7 in range(v_range[6]):
							for S8 in range(v_range[7]):
								for S9 in range(v_range[8]):
									for S10 in range(v_range[9]):
										for S11 in range(v_range[10]):
											for S12 in range(v_range[11]):
												for S13 in range(v_range[12]):
													for S14 in range(v_range[13]):
														for S15 in range(v_range[14]):
															for S16 in range(v_range[15]):
																for S17 in range(v_range[16]):
																	for S18 in range(v_range[17]):
																		if v_range[0] != 1 and v_range[1] != 1 and  S1 == 0 and S2 == 0:
																			continue
																		elif v_range[0] != 1 and S1 == 0 and id[1] == '0':
																			continue
																		elif v_range[1] != 1 and S2 == 0 and id[0] == '0':
																			continue
																		if v_range[2] != 1 and v_range[3] != 1 and S3 == 0 and S4 == 0:
																			continue
																		elif v_range[2] != 1 and S3 == 0 and id[3] == '0':
																			continue
																		elif v_range[3] != 1 and S4 == 0 and id[2] == '0':
																			continue
																		if v_range[7] != 1 and S8 == 0:
																			continue
																		
																		if (S3 == 1 or id[2] == '1') and (S4 > 2 or (id[3] != 'B' and id[3] > '2')):
																			continue
																		# 1,3,5,7,8,10,12 --- 31day
																		big = [1, 3, 5, 7, 8]
																		s_big = ['1', '3', '5', '7', '8']
																		if S4 in big or id[3] in s_big:
																			if (S1 == 3  or id[0] == '3') and (S2 > 1 or (id[1] != 'B' and id[1] > '1')):
																				continue
																		if (S3 == 1 or id[2] == '1') and (S4 == 0 or S4 == 2 or id[3] == '0' or id[3] == '2'):
																			if (S1 == 3  or id[0] == '3') and (S2 > 1 or (id[1] != 'B' and id[1] > '1')):
																				continue
																		# 4 6 9 11 --- 30day
																		small = [4, 6, 9]
																		s_small = ['4', '6', '9']
																		if S4 in small or id[3] in s_small:
																			if (S1 == 3 or id[0] == '3') and (S2 > 0 or (id[1] != 'B' and id[1] > '0')):
																				continue
																		if (S3 == 1 or id[2] == '1') and (S4 == 1 or id[3] == '1'):
																			if (S1 == 3 or id[0] == '3') and (S2 > 0 or (id[1] != 'B' and id[1] > '0')):
																				continue
																		# leap year
																		if (S3 == 0 or id[2] == '0') and (S4 == 2 or id[3] == '2'):
																			if id[4] == 'B':
																				year.append(S5)
																			else:
																				year.append(id[4])
																			if id[5] == 'B':
																				year.append(S6)
																			else:
																				year.append(id[5])
																			if id[6] == 'B':
																				year.append(S7)
																			else:
																				year.append(id[6])
																			if id[7] == 'B':
																				year.append(S8)
																			else:
																				year.append(id[7])
																			tmp_year = int(year[0])*1000 + int(year[1])*100 + int(year[2])*10 + int(year[3])
																			if (tmp_year/4 == 0 and tmp_year/100 != 0 or tmp_year/400 == 0):
																				if (S1 > 2 or (id[0] != 'B' and id[0] > '2')):
																					continue
																			else:
																				if (S1 > 2 or (id[0] != 'B' and id[0] > '2') or ((S1 == 2 or id[0] == '2') and (S2 > 8 or (id[1] != 'B'  and id[1] > '8')))):
																					continue
																		
																		TMP = 10*S1+9*S2+8*S3+7*S4+6*S5+5*S6+4*S7+3*S8+2*S9+10*S10+9*S11+8*S12+7*S13+6*S14+5*S15+4*S16+3*S17+2*S18
																		H = (TMP + static_value) % 19
																		if H <= 9:
																			calc_A = H
																		else:
																			calc_A = 19 - H
																		if index[-1] != 18:
																			if calc_A == int(A):
																				cases_num += 1
																		else:
																			for i in range(10):
																				if i == calc_A:
																					cases_num += 1
																					break
print cases_num

'''
Appendix test case
#test 1: 6
11111111B1111111116

#test 2: 28
BB0220051234567890B
'''