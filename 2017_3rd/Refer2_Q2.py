#!/usr/bin/python
# -*- coding: UTF-8 -*-
import string
import datetime
str = raw_input().split(',');
gems = '';
for s in str:
	gems = gems+s;
	
def find_last(string,str):
    last_position=-1
    while True:
        position=string.find(str,last_position+1)
        if position==-1:
            return last_position
        last_position=position
def get_max_value(text):
	return max(string.ascii_uppercase, key=text.count);
def get_max_mark(text):
	sp = get_max_value(text);
	tempmark = text.count(sp)*text.count(sp);
	if(text.count(sp)==len(text)):
		return tempmark;
	else:
		s1 = text[:text.index(sp)];
		s2 = text[find_last(text,sp)+1:];
		ts = s1 + s2;
		tc = text[text.index(sp):find_last(text,sp)+1];
		for t2 in tc.split(sp):
			if t2=='':
				continue;
			else:
				tempmark = tempmark + get_max_mark(t2);
		tempmark = tempmark + get_max_mark(ts);
		return tempmark;

def get_div_list(text):	
	posList = [];
	lenList = [];
	count = 0;
	while(count<len(text)):
		posList.append(count);
		templen = 1;
		while(count<len(text)-1):
			if(text[count]==text[count+1]):
				templen = templen + 1;
				count = count + 1;
			else:
				break;
		lenList.append(templen);
		count = count + 1;
	return posList,lenList;

def get_max_score(text):
	maxscore = 0;
	for i in range(26):
		mi = text.count(chr(i+65));
		if(mi>0):
			maxscore = maxscore + mi*mi;
	return maxscore;

def get_current_score(lenList):
	curscore = 0;
	for len in lenList:
		curscore = curscore + len*len;
	return curscore;

def pre_cal(text):
	score = 0;
	while(len(text)>0):
		posList = [];
		lenList = [];
		box = '';
		flag = 0;
		(posList,lenList) = get_div_list(text);
		if(len(posList)==1):
			break;
		for i in range(len(posList)):
			newtext = text[:posList[i]] + text[(posList[i]+lenList[i]):];
			if text[posList[i]] in newtext:
				box = box + text[posList[i]:(posList[i]+lenList[i])];
			else:
				score = score + lenList[i]*lenList[i];
				flag = 1;
		if(flag == 1):
			text = box[:];
		else:
			break;
	return text,score;

def adjust_gems(text,pos,len):
	newtext = text[:pos] + text[(pos+len):];
	ntext,nscore = pre_cal(newtext);
	return ntext,nscore;

def dy_cal(maxList,textList,scoreList,count):
	resultList = [];
	for k in range(len(maxList)):
		resultList.append(maxList[k]+scoreList[k]);
	maxresult = max(resultList);
	i = resultList.index(maxresult);
	maxscore = maxList[i];
	text = textList[i];
	score = scoreList[i];
	posList = [];
	lenList = [];
	(posList,lenList) = get_div_list(text);
	if(get_current_score(lenList)==get_max_score(text)):
		print score+get_current_score(lenList);
		exit(0);
	else:
		del maxList[i];
		del textList[i];
		del scoreList[i];
		for j in range(len(posList)):
			tmptext,tscore = adjust_gems(text,posList[j],lenList[j]);
			tmpscore = tscore + score + lenList[j]*lenList[j];
			tmpmax = get_max_score(tmptext);
			flag = 0;
			if tmptext in textList:
				findindex = textList.index(tmptext);
				if(tmpscore>scoreList[findindex]):
					scoreList[findindex] = tmpscore;
			else:
				maxList.insert(0,tmpmax);
				textList.insert(0,tmptext);
				scoreList.insert(0,tmpscore);

slen = len(gems);
b4Time = datetime.datetime.now();
if(slen>40):
	print get_max_mark(gems);
	exit(0);
maxList = [];
textList = [];
scoreList = [];
newtext,newscore = pre_cal(gems);
maxList.append(get_max_score(newtext));
textList.append(newtext);
scoreList.append(newscore);
count = 0;
while((datetime.datetime.now()- b4Time) < datetime.timedelta(milliseconds = 850)):
	count = count + 1;
	dy_cal(maxList,textList,scoreList,count);
print get_max_mark(gems);