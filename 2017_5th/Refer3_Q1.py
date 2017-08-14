#coding=utf8
import sys,os
import itertools
reload(sys)
sys.setdefaultencoding( "utf-8" )

reslist=[]

def GetRes(jz,x0,y0,cc,num):			
	XUNotConnect = lambda x,y,v,z:False if x>=0 and v==z[x][y] else True
	XDNotConnect = lambda x,y,v,z,c:False if x<c and v==z[x][y] else True
	YUNotConnect = lambda x,y,v,z:False if y>=0 and v==z[x][y] else True
	YDNotConnect = lambda x,y,v,z,c:False if y<c and v==z[x][y] else True
	if (XUNotConnect((x0-1),y0,num,jz) and (XDNotConnect((x0+1),y0,num,jz,cc)) and (YUNotConnect(x0,(y0-1),num,jz)) and (YDNotConnect(x0,(y0+1),num,jz,cc)) ):
		return
	if (not XUNotConnect((x0-1),y0,num,jz)):
		if (x0-1,y0) not in reslist:			
			reslist.append((x0-1,y0))
			GetRes(jz,x0-1,y0,cc,num)		
	if (not (XDNotConnect((x0+1),y0,num,jz,cc)) ):	
		if (x0+1,y0) not in reslist:			
			reslist.append((x0+1,y0))
			GetRes(jz,x0+1,y0,cc,num)		
	if (not (YUNotConnect(x0,(y0-1),num,jz)) ):
		if (x0,y0-1) not in reslist:			
			reslist.append((x0,y0-1))
			GetRes(jz,x0,y0-1,cc,num)
	if (not (YDNotConnect(x0,( y0+1),num,jz,cc))) :		
		if (x0,y0+1) not in reslist:
			reslist.append((x0,y0+1))
			GetRes(jz,x0,y0+1,cc,num)

if __name__ == '__main__':
	line1=raw_input().split(' ')
	x0=int(line1[0])
	y0=int(line1[1])
	cc=int(raw_input())
	jz = [[0 for i in range(cc)] for j in range(cc)];
	for i in range(cc):
		linen=raw_input().split(' ')		
		for j in range(cc):
			jz[i][j]=int(linen[j])
	reslist.append((x0,y0))
	GetRes(jz,x0,y0,cc,jz[x0][y0])
	print len(reslist)
	