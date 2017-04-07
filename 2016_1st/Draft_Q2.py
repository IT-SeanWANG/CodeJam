#! /usr/bin/python


#############################################
## Designed by Sean Wang for NOKIA Code Jam
## 2016/08/20
#############################################

print('Welcome to Fight-Landlord!')


### cards info class
class CardsInfo(object):
	# store the start position and length of one kind card[start, length]
	list = [0] * 18
	# store the needed times of one kind card
	times = 0
	# store the number of one kind card
	num = 0
	# indicate whether need to do further calcaulte(ThreeOneTwo/FourTwo/PlaneWing Type)
	ind_flag = False
	
	def ___init__(self):
		self.list = [0 for col in range(18)]
		self.times = 0
		self.num = 0
		self.ind_flag = False


### Covert to number cards
def ToNumCards(cards=[]):
	tmp_num_cards = [0] * 17
	for i in range(17):
		if cards[i] == 'W':
			#cards.replace(cards[i], '1')
			tmp_num_cards[i] = 1
		elif cards[i] == 'S':
			tmp_num_cards[i] = 10
		elif cards[i] == 'J':
			tmp_num_cards[i] = 11
		elif cards[i] == 'Q':
			tmp_num_cards[i] = 12
		elif cards[i] == 'K':
			tmp_num_cards[i] = 13
		elif cards[i] == 'A':
			tmp_num_cards[i] = 14
		else:
			tmp_num_cards[i] = int(cards[i])
	#print "tmp_num_cards: %s" %tmp_num_cards
	return tmp_num_cards


### Bucket sort algorithm for 17 cards
def SortCards(cards=[]):
	tmp_sort_cards = [0] * 18
	for i in range(len(cards)):
		tmp_sort_cards[cards[i]] += 1
	#Only 14 type cards except index 0
	#print "tmp_sort_cards: %s" %tmp_sort_cards
	return tmp_sort_cards


# Covert to viewable cards
def ToAlphaCards(cards):
	tmp_cards = ''
	
	for i in range(1, 17):
		if cards == 1:
			tmp_cards = 'W'
		elif cards == 10:
			tmp_cards = 'S'
		elif cards == 11:
			tmp_cards = 'J'
		elif cards == 12:
			tmp_cards = 'Q'
		elif cards == 13:
			tmp_cards = 'K'
		elif cards == 14:
			tmp_cards = 'A'
		else:
			tmp_cards = str(cards)
	#print(tmp_cards)
	return tmp_cards

	
### Cards Type: PlaneWing; Weight: 10(8+/time[444555+68/777888999+335566/... except 2 and Kings])
# Input: sort cards
# Output: start position, max PlaneWing length and left cards
def PlaneWingCards(cards=[]):
	tmp_cards_info10 = CardsInfo()
	#init list
	tmp_cards_info10.list = [0]*18
	tmp_cards_info10 = SanShunCards(cards)
	if tmp_cards_info10.times != 0:
		tmp_cards_info10.ind_flag = True
	
	#print "PlaneWingCards"
	#print "PlaneWingCards: tmp_cards_info10.list: %s tmp_cards_info10.num: %d  tmp_cards_info10.times: %d left cards: %s" %(tmp_cards_info10.list, tmp_cards_info10.num, tmp_cards_info10.times, cards)
	return tmp_cards_info10


### Cards Type: SanShun; Weight: 9(6+/time[444555/777888999/... except 2 and Kings])
# Input: sort cards(cards[])
# Output: start position, length, numbers and left cards(cards[])
def SanShunCards(cards=[]):
	tmp_cards_info9 = CardsInfo()
	#init list
	tmp_cards_info9.list = [0]*18
	tmp_start = 0
	tmp_len = 0
	
	# 0, King and 2 not included
	for i in range(3, len(cards)):
		for j in range(i, len(cards)):
			# 3 same cards
			if cards[j] >= 3:
				tmp_len += 1
				# length >= 2
				if tmp_len < 2:
					continue
				else:
					tmp_start = i
			else:
				if (tmp_start) and (tmp_cards_info9.list[tmp_start] <= tmp_len):
					tmp_cards_info9.list[tmp_start] = tmp_len
					tmp_cards_info9.num += tmp_len * 3
					tmp_cards_info9.times += 1
					# remove this time SanShun from cards
					for k in range(i, i + tmp_len):
						cards[k] -= 3
				tmp_start = 0
				tmp_len = 0
				break
	#print "SanShunCards: tmp_cards_info9.list: %s tmp_cards_info9.num: %d  tmp_cards_info9.times: %d left cards: %s" %(tmp_cards_info9.list, tmp_cards_info9.num, tmp_cards_info9.times, cards)
	return tmp_cards_info9


### Cards Type: ShuangShun; Weight: 8(6+/time[445566/7788991010/... except 2 and Kings])
# Input: sort cards(cards[])
# Output: start position, length, numbers and left cards(cards[])
def ShuangShunCards(cards=[]):
	tmp_cards_info8 = CardsInfo()
	#init list
	tmp_cards_info8.list = [0]*18
	tmp_start = 0
	tmp_len = 0
	
	# 0, King and 2 not included
	for i in range(3, len(cards)):
		for j in range(i, len(cards)):
			# 2 same cards
			if cards[j] >= 2:
				tmp_len += 1
				# length >= 3
				if tmp_len < 3:
					continue
				else:
					tmp_start = i
			else:
				if (tmp_start) and (tmp_cards_info8.list[tmp_start] <= tmp_len):
					tmp_cards_info8.list[tmp_start] = tmp_len
					tmp_cards_info8.num += tmp_len * 2
					tmp_cards_info8.times += 1
					# remove this time ShuangShun from cards
					for k in range(i, i + tmp_len):
						cards[k] -= 2
				tmp_start = 0
				tmp_len = 0
				break
	#print "ShuangShunCards: tmp_cards_info8.list: %s tmp_cards_info8.num: %d  tmp_cards_info8.times: %d left cards: %s" %(tmp_cards_info8.list, tmp_cards_info8.num, tmp_cards_info8.times, cards)
	return tmp_cards_info8


### Cards Type: DanShun; Weight: 7(5+/time[34567/8910JQKA/... except 2 and Kings])
# Input: sort cards(cards[])
# Output: start position, length, numbers and left cards(cards[])
def DanShunCards(cards=[]):
	tmp_cards_info7 = CardsInfo()
	#init list
	tmp_cards_info7.list = [0]*18
	tmp_start = 0
	tmp_len = 0
	
	# 0, King and 2 not included
	for i in range(3, len(cards)):
		for j in range(i, len(cards)):
			# 1 same card
			if cards[j] >= 1:
				tmp_len += 1
				#print "tmp_len: %d" %(tmp_len)
				# length >= 5
				if tmp_len < 5:
					continue
				else:
					tmp_start = i
			else:
				if (tmp_start) and (tmp_cards_info7.list[tmp_start] <= tmp_len):
					tmp_cards_info7.list[tmp_start] = tmp_len
					tmp_cards_info7.num += tmp_len
					tmp_cards_info7.times += 1
					# remove this time DanShun from cards
					for k in range(i, i + tmp_len):
						cards[k] -= 1
				tmp_start = 0
				tmp_len = 0
				break
	#print "DanShunCards: tmp_cards_info7.list: %s tmp_cards_info7.num: %d  tmp_cards_info7.times: %d left cards: %s" %(tmp_cards_info7.list, tmp_cards_info7.num, tmp_cards_info7.times, cards)
	return tmp_cards_info7


### Cards Type: FourTwo; Weight: 6(6~8/time[4444+57/8888+3355/...])
# Input: sort cards(cards[])
# Output: start position, length, numbers and left cards(cards[])
def FourTwoCards(cards=[]):
	tmp_cards_info6 = CardsInfo()
	#init list
	tmp_cards_info6.list = [0]*18
	
	tmp_cards_info6 = FourCards(cards)
	if tmp_cards_info6.times != 0:
		tmp_cards_info6.ind_flag = True
	
	#print "FourTwoCards"
	#print "FourTwoCards: tmp_cards_info6.list: %s tmp_cards_info6.num: %d  tmp_cards_info6.times: %d left cards: %s" %(tmp_cards_info6.list, tmp_cards_info6.num, tmp_cards_info6.times, cards)
	return tmp_cards_info6



### Cards Type: ThreeOneTwo; Weight: 5(4~5/time[333+6/444+99/...])
# Input: sort cards(cards[])
# Output: start position, length, numbers and left cards(cards[])
def ThreeOneTwoCards(cards=[]):
	tmp_cards_info5 = CardsInfo()
	#init list
	tmp_cards_info5.list = [0]*18
	
	tmp_cards_info5 = ThreeCards(cards)
	if tmp_cards_info5.times != 0:
		tmp_cards_info5.ind_flag = True
	
	#print "ThreeOneTwoCards"
	#print "ThreeOneTwoCards: tmp_cards_info5.list: %s tmp_cards_info5.num: %d  tmp_cards_info5.times: %d left cards: %s" %(tmp_cards_info5.list, tmp_cards_info5.num, tmp_cards_info5.times, cards)
	return tmp_cards_info5


### Cards Type: Four; Weight: 4(4/time[3333/7777/...])
# Input: sort cards(cards[])
# Output: start position, length, numbers and left cards(cards[])
def FourCards(cards=[]):
	tmp_cards_info4 = CardsInfo()
	#init list
	tmp_cards_info4.list = [0]*18
	
	tmp_flag = False
	tmp_len = 0
	
	#  0 not included
	for i in range(1, len(cards)):
		if (cards[i] == 4):
			tmp_cards_info4.list[i] = 1
			tmp_cards_info4.num += 4
			tmp_cards_info4.times += 1
			# remove counted cards
			cards[i] -= 4
	
	#print "FourCards: tmp_cards_info4.list: %s tmp_cards_info4.num: %d  tmp_cards_info4.times: %d left cards: %s" %(tmp_cards_info4.list, tmp_cards_info4.num, tmp_cards_info4.times, cards)
	return tmp_cards_info4


### Cards Type: Three; Weight: 3(3/time[444/666/...])
# Input: sort cards(cards[])
# Output: start position, length, numbers and left cards(cards[])
def ThreeCards(cards=[]):
	tmp_cards_info3 = CardsInfo()
	#init list
	tmp_cards_info3.list = [0]*18
	
	tmp_flag = False
	tmp_len = 0
	
	#  0 not included
	for i in range(1, len(cards)):
		# King and 2
		if i<= 2:
			if (cards[i] == 3):
				tmp_cards_info3.list[i] = 1
				tmp_cards_info3.num += 3
				tmp_cards_info3.times += 1
				# remove counted cards
				cards[i] -= 3
		# 3 ~ 4
		elif i<= 4:
			m = 3
			n = i + 1
		# 5 ~ K
		elif i <= 13:
			m = i - 1
			n = i + 1
		# A
		elif i <= 14:
			m = i - 1
			n = 14
		else:
			m = 0
			n = 0
		if (cards[i] == 3):
			# search Three type algo
			for j in range(m, n+1):
				if cards[j] == 3:
					tmp_len += 1
					if tmp_len < 2:
						continue
					else:
						# found ShuangShun type
						tmp_flag = True
						break
			if (tmp_flag == False):
				tmp_cards_info3.list[i] = 1
				tmp_cards_info3.num += 3
				tmp_cards_info3.times += 1
				# remove counted cards
				cards[i] -= 3
	
	#print "ThreeCards: tmp_cards_info3.list: %s tmp_cards_info3.num: %d  tmp_cards_info3.times: %d left cards: %s" %(tmp_cards_info3.list, tmp_cards_info3.num, tmp_cards_info3.times, cards)
	return tmp_cards_info3


### Cards Type: Two; Weight: 2(2/time[33/77/....])
# Input: sort cards(cards[])
# Output: start position, length, numbers and left cards(cards[])
def TwoCards(cards=[]):
	tmp_cards_info2 = CardsInfo()
	#init list
	tmp_cards_info2.list = [0]*18
	tmp_flag = False
	tmp_len = 0
	
	#  0 not included
	for i in range(1, len(cards)):
		# King and 2
		if i<= 3:
			if (cards[i] >= 2):
				tmp_cards_info2.list[i] = 1
				tmp_cards_info2.num += 2
				tmp_cards_info2.times += 1
				# remove counted cards
				cards[i] -= 2
		# 4
		elif i<= 4:
			m = i- 1
			n = i + 2
		# 5 ~ Q
		elif i <= 12:
			m = i - 2
			n = i + 2
		# K ~ A
		elif i <= 14:
			m = i - 2
			n = 14
		else:
			m = 0
			n = 0
		if (cards[i] >= 2):
			# search Two type algo
			for j in range(m, n+1):
				if cards[j] >= 2:
					tmp_len += 1
					if tmp_len < 3:
						continue
					else:
						# found ShuangShun type
						tmp_flag = True
						break
			if (tmp_flag == False):
				tmp_cards_info2.list[i] = 1
				tmp_cards_info2.num += 2*tmp_len
				tmp_cards_info2.times += 1*tmp_len
				# remove counted cards
				cards[i] -= 2
	
	#print "TwoCards: tmp_cards_info2.list: %s tmp_cards_info2.num: %d  tmp_cards_info2.times: %d left cards: %s" %(tmp_cards_info2.list, tmp_cards_info2.num, tmp_cards_info2.times, cards)
	return tmp_cards_info2


### Cards Type: One; Weight: 1(1/time[8/J/...])
# Input: sort cards(cards[])
# Output: start position, length, numbers and left cards(cards[])
def OneCards(cards=[]):
	tmp_cards_info1 = CardsInfo()
	#init list
	tmp_cards_info1.list = [0]*18
	tmp_flag = False
	tmp_len = 0
	
	#  0 not included
	for i in range(1, len(cards)):
		# King and 2
		if i<= 2:
			if (cards[i] == 1):
				tmp_cards_info1.list[i] = 1
				tmp_cards_info1.num += 1
				tmp_cards_info1.times += 1
				# remove counted cards
				cards[i] -= 1
		# 3 ~ 7
		elif i<= 7:
			m = 3
			n = i + 4
		# 8 ~ 10
		elif i <= 10:
			m = i - 4
			n = i
		# J ~ A
		elif i <= 14:
			m = i - 4
			n = 14
		else:
			m = 0
			n = 0
		if (cards[i] == 1):
			# search One type algo
			for j in range(m, n+1):
				if cards[j] >= 1:
					tmp_len += 1
					if tmp_len < 5:
						continue
					else:
						# found DanShun type
						tmp_flag = True
						break
			if (tmp_flag == False):
				tmp_cards_info1.list[i] = 1
				tmp_cards_info1.num += 1
				tmp_cards_info1.times += 1
				# remove counted cards
				cards[i] -= 1
				tmp_len = 0
	
	#print "OneCards: tmp_cards_info1.list: %s tmp_cards_info1.num: %d  tmp_cards_info1.times: %d left cards: %s" %(tmp_cards_info1.list, tmp_cards_info1.num, tmp_cards_info1.times, cards)
	return tmp_cards_info1


# return the min play hand times and corresponding cards
# Input: 17 cards
# Output: -
def PlayCard(input_cards = []):
	num_cards = [0] * 17
	# for sort cards, 0 not used
	sort_cards = [0] * 18
	tmp_sort_cards = [0] * 18
	# the rests of one kind card
	left_num = 0
	cards_info = CardsInfo()
	# cross cards type
	cards_info_w10 = CardsInfo()   #PlaneWing
	cards_info_w9 = CardsInfo()    #SanShun
	cards_info_w8 = CardsInfo()    #ShuangShun
	cards_info_w7 = CardsInfo()    #DanShun
	
	cards_info_w6 = CardsInfo()    #FourTwo
	cards_info_w5 = CardsInfo()    #ThreeOneTwo
	cards_info_w4 = CardsInfo()    #Four
	cards_info_w3 = CardsInfo()    #Three
	cards_info_w2 = CardsInfo()    #Two
	
	cards_info_w1 = CardsInfo()    #One
	
	out_cards_str = ''
	out_cards_times = 0
	
	# cards preprocess
	num_cards = ToNumCards(input_cards)
	#print "num_cards: %s" %num_cards
	
	sort_cards = SortCards(num_cards)
	tmp_sort_cards = sort_cards
	#print "sort_cards: %s tmp_sort_cards: %s" %(sort_cards, tmp_sort_cards)
	
	# loop search the min combine, need to finish once all cards type interface finished
	# step1 remove OneCards type due to no connect with others
	'''cards_info = OneCards(sort_cards)
	out_cards_times = cards_info.times'''
	
	# should be only below types need to combine with orders....
		# PlaneWing(8+) 1st
		# SanShun(6+) 1st
		# ShuangShun(6+) 1st
		# DanShun(5+) 1st
		# FourTwo(6~8) 1st
	# for sort usage
	#tmp_list = [[0 for col in range(3)] for row in range(10)]
	cards_list = [['PlaneWingCards',0,0], ['SanShunCards',0,0], ['ShuangShunCards',0,0], ['DanShunCards',0,0], ['FourTwoCards',0,0], ['ThreeOneTwoCards',0,0], ['FourCards',0,0], ['ThreeCards',0,0], ['TwoCards',0,0], ['OneCards',0,0]]
	swap_list = [0] * 3
	
	# step2-1 search PlaneWingCards type firstly(create one sort_cards copy instead of printer)
	'''tmp_sort_cards = sort_cards[:]
	cards_info_w10 = PlaneWingCards(tmp_sort_cards)
	cards_list[0][0] = 'PlaneWingCards' '''
	#min number for PlaneWingCards
	'''cards_list[0][1] = cards_info_w10.num + 2*cards_info_w10.times
	cards_list[0][2] = cards_info_w10.times'''
	
	
	# step2-2 search SanShunCards type firstly

	tmp_sort_cards = sort_cards[:]
	'''cards_info_w9 = SanShunCards(tmp_sort_cards)
	cards_list[1][0] = 'SanShunCards'
	cards_list[1][1] = cards_info_w9.num
	cards_list[1][2] = cards_info_w9.times'''
	
	
	
	# step2-3 search ShuangShunCards type firstly
	'''tmp_sort_cards = sort_cards[:]
	cards_info_w8 = ShuangShunCards(tmp_sort_cards)
	cards_list[2][0] = 'ShuangShunCards'
	cards_list[2][1] = cards_info_w8.num
	cards_list[2][2] = cards_info_w8.times'''
	
	# step2-4 search DanShunCards type firstly
	'''tmp_sort_cards = sort_cards[:]
	cards_info_w7 = DanShunCards(tmp_sort_cards)
	cards_list[3][0] = 'DanShunCards'
	cards_list[3][1] = cards_info_w7.num
	cards_list[3][2] = cards_info_w7.times'''
	
	#print "-----sort_cards: %s" %(sort_cards)
	# step2-5 sort each types
	#print "before cards_list: %s" %(cards_list)
	'''for i in range(4):
		for j in range(i+1, 4):
			if (cards_list[i][2] == 0) or (cards_list[j][2] == 0):
				continue
			# max numbers and min times of play a hand(average)
			if (cards_list[i][1]/cards_list[i][2] + cards_list[i][1]%cards_list[i][2]) >= (cards_list[j][1]/cards_list[j][2] + cards_list[j][1]%cards_list[j][2]):
				continue
			else:
				swap_list[0] = cards_list[i][0]
				cards_list[i][0] = cards_list[j][0]
				cards_list[j][0] = swap_list[0]
				
				swap_list[1] = cards_list[i][1]
				cards_list[i][1] = cards_list[j][1]
				cards_list[j][1] = swap_list[1]
				
				swap_list[2] = cards_list[i][2]
				cards_list[i][2] = cards_list[j][2]
				cards_list[j][2] = swap_list[2]'''
	#print "after cards_list: %s" %(cards_list)
	
	# step3 compare above solutions and print the min combine(using sort_cards indeed)
	tmp_sort_cards = sort_cards
	#print "********sort_cards: %s tmp_sort_cards: %s" %(sort_cards, tmp_sort_cards)
	#print "Marker tmp_sort_cards: %s cards_list[0][0]: %s" %(sort_cards, cards_list[0][0])
	out_info = [[0 for col in range(2)] for row in range(18)] 
	rep_flag = 0
	tmp_out_cards_str = ''
	refer_num = 17
	for case in range(10):
		#print "Marker ############################case: %d" %case
		for i in range(10):
			cards_info = eval(cards_list[i][0])(tmp_sort_cards)
			out_cards_times += cards_info.times
			if (cards_info.ind_flag == True) and (cards_list[i][0] == 'ThreeOneTwoCards'):
				#print "ThreeOneTwoCards.........."
				for j in range(18):
					n = cards_info.list[j]
					for k in range (n):
						for l in range (3):
							out_cards_str += ToAlphaCards(j)
						# print blank symbol
						if k == (n - 1):
							out_cards_str += ' '
				cards_info_w5 = cards_info
				#print "%%%%%%%%%%%%%%%%%%%%out_cards_str:%s" %out_cards_str
			elif (cards_info.ind_flag == True) and (cards_list[i][0] == 'FourTwoCards'):
				#print "FourTwoCards.........."
				for j in range(18):
					n = cards_info.list[j]
					for k in range (n):
						for l in range (4):
							out_cards_str += ToAlphaCards(j)
						# print blank symbol
						if k == (n - 1):
							out_cards_str += ' '
				cards_info_w6 = cards_info
				#print "%%%%%%%%%%%%%%%%%%%%out_cards_str:%s" %out_cards_str
			elif (cards_info.ind_flag == True) and (cards_list[i][0] == 'PlaneWingCards'):
				#print "PlaneWingCards.........."
				for j in range(18):
					n = cards_info.list[j]
					for k in range (n):
						for l in range (3):
							out_cards_str += ToAlphaCards(j + k)
						# print blank symbol
						if k == (n - 1):
							out_cards_str += ' '
				cards_info_w10 = cards_info
				#print "%%%%%%%%%%%%%%%%%%%%out_cards_str:%s" %out_cards_str
			elif (cards_list[i][0] == 'SanShunCards'):
				#print "SanShunCards.........."
				for j in range(18):
					n = cards_info.list[j]
					for k in range (n):
						for l in range (3):
							out_cards_str += ToAlphaCards(j + k)
						# print blank symbol
						if k == (n - 1):
							out_cards_str += ' '
				#print "%%%%%%%%%%%%%%%%%%%%out_cards_str:%s" %out_cards_str
			elif (cards_list[i][0] == 'ShuangShunCards'):
				#print "ShuangShunCards.........."
				for j in range(18):
					n = cards_info.list[j]
					for k in range (n):
						for l in range (2):
							out_cards_str += ToAlphaCards(j + k)
						# print blank symbol
						if k == (n - 1):
							out_cards_str += ' '
				#print "%%%%%%%%%%%%%%%%%%%%out_cards_str:%s" %out_cards_str
			elif (cards_list[i][0] == 'DanShunCards'):
				#print "DanShunCards.........."
				for j in range(18):
					n = cards_info.list[j]
					for k in range (n):
						out_cards_str += ToAlphaCards(j + k)
						# print blank symbol
						if k == (n - 1):
							out_cards_str += ' '
				#print "%%%%%%%%%%%%%%%%%%%%out_cards_str:%s" %out_cards_str
			elif (cards_list[i][0] == 'FourCards'):
				#print "FourCards.........."
				for j in range(18):
					n = cards_info.list[j]
					for k in range (n):
						for l in range (4):
							out_cards_str += ToAlphaCards(j)
						# print blank symbol
						if k == (n - 1):
							out_cards_str += ' '
				#print "%%%%%%%%%%%%%%%%%%%%out_cards_str:%s" %out_cards_str
			elif (cards_list[i][0] == 'ThreeCards'):
				#print "ThreeCards.........."
				for j in range(18):
					n = cards_info.list[j]
					for k in range (n):
						for l in range (3):
							out_cards_str += ToAlphaCards(j)
						# print blank symbol
						if k == (n - 1):
							out_cards_str += ' '
				#print "%%%%%%%%%%%%%%%%%%%%out_cards_str:%s" %out_cards_str
			elif (cards_list[i][0] == 'TwoCards'):
				#print "TwoCards..........n:%d" %n
				for j in range(18):
					n = cards_info.list[j]
					for k in range (n):
						for l in range (2):
							out_cards_str += ToAlphaCards(j + k)
						# print blank symbol
						if k == (n - 1):
							out_cards_str += ' '
				cards_info_w2 = cards_info
				#print "%%%%%%%%%%%%%%%%%%%%out_cards_str:%s" %out_cards_str
			elif (cards_list[i][0] == 'OneCards'):
				#print "OneCards.........."
				for j in range(18):
					n = cards_info.list[j]
					for k in range (n):
						out_cards_str += ToAlphaCards(j + k)
						# print blank symbol
						if k == (n - 1):
							out_cards_str += ' '
				cards_info_w1 = cards_info
				#print "%%%%%%%%%%%%%%%%%%%%out_cards_str:%s" %out_cards_str
				
		tmp_cards_times = out_cards_times
		if cards_info_w10.times != 0:
			tmp_i = (2*cards_info_w10.num/3 + cards_info_w6.times*2 + cards_info_w5.times)
		else:
			tmp_i = (cards_info_w6.times*2 + cards_info_w5.times)
		tmp_j = (cards_info_w1.times + cards_info_w2.times)
		tmp_k = cards_info_w10.times + cards_info_w6.times + cards_info_w5.num
		if (tmp_i > tmp_j):
			tmp_cards_times -= tmp_j
		else:
			tmp_cards_times -= tmp_k
			
		swap_list[0] = cards_list[0][0]
		cards_list[0][0] = cards_list[case][0]
		cards_list[case][0] = swap_list[0]
		swap_list[1] = cards_list[0][1]
		cards_list[0][1] = cards_list[case][1]
		cards_list[case][1] = swap_list[1]
		swap_list[2] = cards_list[0][2]
		cards_list[0][2] = cards_list[case][2]
		cards_list[case][2] = swap_list[2]
		if tmp_cards_times < refer_num:
			#print "1%%%%%%%%%%%%%%%%%%%%tmp_cards_times:%d refer_num: %d" %(tmp_cards_times, refer_num)
			# only store one minimum type
			out_info[0][0] = tmp_cards_times
			out_info[0][1] = out_cards_str
			tmp_out_cards_str = out_cards_str
			refer_num = tmp_cards_times
		elif tmp_cards_times == refer_num:
			#print "2%%%%%%%%%%%%%%%%%%%%tmp_cards_times:%d" %(tmp_cards_times)
			if (out_cards_str != tmp_out_cards_str):
				#print "%%%%%%%%%%%%%%%%%%%%out_cards_str:%s %s" %(out_cards_str, tmp_out_cards_str)
				rep_flag += 1
				out_info[rep_flag][0] = tmp_cards_times
				out_info[rep_flag][1] = out_cards_str
		else:
			#print "3%%%%%%%%%%%%%%%%%%%%tmp_cards_times:%d" %(tmp_cards_times)
			refer_num = tmp_cards_times
		
		
	#print "Marker sort_cards: %s" %(tmp_sort_cards)
	#print "cards_info.list: %s cards_info.num: %d sort_cards: %s" %(cards_info.list, cards_info.num, sort_cards)
	
	# print the min hand times and corresponding cards before add One/Two cards to PlaneWing/FourTwo/ThreeOneTwo Cards
	for i in range(17):
		if (out_info[i+1][0] != 0) and (out_info[i][0] == out_info[i+1][0]):
			print "Minimum Type Number:%d" %out_info[i][0]
			print "Minimum Type Detail:%s" %out_info[i][1]
		else:
			print "Minimum Type Number:%d" %out_info[0][0]
			print "Minimum Type Detail:%s" %out_info[0][1]
			break
	
	# print the min hand times and corresponding cards before add One/Two cards to PlaneWing/FourTwo/ThreeOneTwo Cards
	'''out_cards_str.strip()
	split_list = out_cards_str.split( )
	for i in range(out_cards_times):
		print(split_list[i])
		
	print "Minimum Type Number:%d" %out_cards_times
	print "Minimum Type Detail:%s" %(out_cards_str[0])'''



### Main Entry
#cards = [1, 2, 3, 4, 5, 6, 7, 7, 9, 9, 'S', 'J', 4, 'K', 'A', 'Q', 'Q']

# input cards
cards = []
while len(cards) != 17:
	cards = raw_input("Please input 17 cards(range 2-9 S[10] J-A W[King]): ")
PlayCard(cards)

## only used for card type algo test
'''num_cards = [0] * 17
sort_cards = [0] * 18
num_cards = ToNumCards(cards)
sort_cards = SortCards(num_cards)
tmp_sort_cards = sort_cards'''
#print "sort_cards: %s tmp_sort_cards: %s" %(sort_cards, tmp_sort_cards)
#cards_info = PlaneWingCards(sort_cards)
#cards_info = SanShunCards(sort_cards)
#cards_info = ShuangShunCards(sort_cards)
#cards_info = DanShunCards(sort_cards)
#cards_info = FourTwoCards(sort_cards)
#cards_info = ThreeOneTwoCards(sort_cards)
#cards_info = FourCards(sort_cards)
#cards_info = ThreeCards(sort_cards)
#cards_info = TwoCards(sort_cards)
#cards_info = OneCards(sort_cards)
#print "cards_info.list: %s cards_info.num: %d  cards_info.times: %d sort_cards: %s" %(cards_info.list, cards_info.num, cards_info.times, sort_cards)

