#coding=utf8
import sys,os
from itertools import *
import itertools
import copy
reload(sys)
sys.setdefaultencoding( "utf-8" )

comPi=[]	
dPi=[]
resL=[]

def GetdPi(m,pis,n):
	for i in range(1,n+1):
		if (i<=m):
			cc=pis[:i]
			tol=sum(cc)
			y=sum([ j%m for j in cc])
			#s=(sum(cc)-y)/m
			s=tol/m
			#tt=sum[x%s for x in cc]
			while [ 1 ]:
				if (tol-sum([j%s for j in cc])) < s*m:
					s-=1
				else:
					break
			dPi.append([i,(tol-sum([j%s for j in cc]))/m])
def getKey( x ):  
    return x[1]
	
def getKey0( x ):  
    return x[0]
		
if __name__ == '__main__':
	line1=raw_input().split(' ')
	lab=int(line1[0])
	comP=int(line1[1])
	line2=raw_input().split(' ')
	for i in range(comP):
		comPi.append(int(line2[i]))
	comPi.sort(reverse=True)
	GetdPi(lab,comPi,comP)	
	dPi.sort(key=getKey,reverse=True)
	maxL=0
	for tt in dPi:
		maxL=tt[1]
		dPiNew=filter(lambda x:x[1]==maxL , dPi)
		for i in dPiNew:
			L=i[1]
			k=i[0]
			if (k<=lab):	
				Llist=list(itertools.combinations(filter(lambda x:x>=L, comPi),k))	
				if (len(Llist)>0):
					aa=0
					#Llist1=[sum(x) for x in Llist]					
					Llist1=map(lambda u:u[0],filter(lambda y:(y[0]-y[1])>=lab*L,map(lambda x:[sum(x),sum(t%L for t in x)],Llist))  )
					if (len(Llist1)>0):
						resL.extend([[k,min(Llist1),L]])  #here need varify the tuple is suitable eg: 8 6 4 is not suitable										
		if (len(resL)>0):
			break	
	#resL.sort(key=getKey0,reverse=True)
	resL.sort(key=getKey)
	if (len(resL)>0):
		print "%d %d"%(resL[0][2],resL[0][1])
	

