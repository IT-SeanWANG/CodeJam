#!/usr/bin/python
# -*- coding: UTF-8 -*-
ID=raw_input();

dMod = 19;
dp = [[-1 for i in range(19)] for j in range(19)];
hash = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10];
dt = [-1 for i in range(8)];
#ID="BBBBBBBBBBBBBBBBBBB";
lenID=18;
#采用数位dp计算，同时对前8位日期判断从而进行剪枝
def dfs(pos, mod, dt, limit):
	H = mod;
	if(H>9):
		H = 19-H;
	ans = 0;
	if(pos==0):
		if(ID[18]!='B'):			
			if(H==int(ID[18])):
				return 1;
			else:
				return 0;
		else:
			return 1;
	if(lenID-pos>=4 and limit==0 and dp[pos][mod]!=-1):
		return dp[pos][mod];
		
	if(ID[lenID-pos]=='B'):
		num = [];
		if(pos==lenID):
			num=range(4);
			if(ID[1]=='0'):
				num.remove(0);
			if(ID[2]=='0' and ID[3]=='2'):
				num.remove(3);
		#月份也应该去掉00
		elif(pos==lenID-1):
			if(dt[0]==0):
				num=range(1,10);
			elif(dt[0]==1 or dt[0]==2):
				num=range(10);
			else:
				num=range(2);
		elif(pos==lenID-2):
			num=range(2);
			'''加上这句就可以了
			if(ID[3]=='0'):
				num.remove(0);
			'''
		elif(pos==lenID-3):
			if(dt[2]==0):
				if(dt[0]==3 and dt[1]==1):
					num=[1,3,5,7,8];
				elif(dt[0]==3 and dt[1]==0):
					num=[1,3,4,5,6,7,8,9];
				else:
					num=range(1,10);
			else:
				if(dt[0]==3 and dt[1]==1):
					num=[0,2];
				else:
					num=[0,1,2];
		else:
			num = range(10);
			
		for i in num:
			dt2 = dt[:];
			if(lenID-pos<8):
				dt2[lenID-pos]=i;
			if(lenID-pos<4):
				ans+=dfs(pos-1,(mod+i*hash[pos-1])%dMod,dt2,1);
				#根据(A+B)%等价于A%+B%，可以把上一数位的mod计算之后传给下一数位，这样避免了重复计算
			else:
				#剪枝部分处理的不好
				if(limit==1 and dt2[0]==3 and dt2[2]==0 and dt2[3]==2):
					False;
				elif(limit==1 and dt2[0]==3 and dt2[1]==1 and dt2[2]==0 and dt2[3]==4):
					False;
				elif(limit==1 and dt2[0]==3 and dt2[1]==1 and dt2[2]==0 and dt2[3]==6):
					False;
				elif(limit==1 and dt2[0]==3 and dt2[1]==1 and dt2[2]==0 and dt2[3]==9):
					False;
				elif(limit==1 and dt2[0]==3 and dt2[1]==1 and dt2[2]==0 and dt2[3]==11):
					False;
				elif(limit==1 and lenID-pos<8 and dt2[lenID-pos]==0):
					ans+=dfs(pos-1,(mod+i*hash[pos-1])%dMod,dt2,1);
				elif(limit==1 and lenID-pos==5 and dt2[5]==0):
					ans+=dfs(pos-1,(mod+i*hash[pos-1])%dMod,dt2,1);	
				else:
					if(limit==1 and dt2[0]==2 and dt2[1]==9 and dt2[2]==0 and dt2[3]==2):
						if(lenID-pos<7):
							ans+=dfs(pos-1,(mod+i*hash[pos-1])%dMod,dt2,1);
						else:
							yearItem = dt2[4]*1000+dt2[5]*100+dt2[6]*10+dt2[7];
							if (((yearItem % 4) == 0 and (yearItem % 100) != 0) or (yearItem % 400) == 0):
								if(yearItem!=0):
									ans += dfs(pos-1,(mod+i*hash[pos-1])%dMod,dt2,0);
					elif(limit==1 and dt[4]==0 and dt[5]==0 and dt[6]==0 and dt[7]==0):
						False;
					else:
						ans+=dfs(pos-1,(mod+i*hash[pos-1])%dMod,dt2,0);
			
	else:
		index = int(ID[lenID-pos]);
		dt2 = dt[:];
		if(lenID-pos<8):
			dt2[lenID-pos]=index;
		if(lenID-pos<4):
			ans+=dfs(pos-1,(mod+index*hash[pos-1])%dMod,dt2,1);
		else:
			if(limit==1 and dt2[0]==3 and dt2[2]==0 and dt2[3]==2):
				False;
			elif(limit==1 and dt2[0]==3 and dt2[1]==1 and dt2[2]==0 and dt2[3]==4):
				False;
			elif(limit==1 and dt2[0]==3 and dt2[1]==1 and dt2[2]==0 and dt2[3]==6):
				False;
			elif(limit==1 and dt2[0]==3 and dt2[1]==1 and dt2[2]==0 and dt2[3]==9):
				False;
			elif(limit==1 and dt2[0]==3 and dt2[1]==1 and dt2[2]==0 and dt2[3]==11):
				False;
			if(limit==1 and lenID-pos<8 and dt2[lenID-pos]==0):
				ans+=dfs(pos-1,(mod+index*hash[pos-1])%dMod,dt2,1);
			else:
				if(limit==1 and dt2[0]==2 and dt2[1]==9 and dt2[2]==0 and dt2[3]==2):
					if(lenID-pos<7):
						ans += dfs(pos-1,(mod+index*hash[pos-1])%dMod,dt2,1);
					else:
						yearItem = dt2[4]*1000+dt2[5]*100+dt2[6]*10+dt2[7];
						if (((yearItem % 4) == 0 and (yearItem % 100) != 0) or (yearItem % 400) == 0):
							if(yearItem!=0):
								ans += dfs(pos-1,(mod+index*hash[pos-1])%dMod,dt2,0);
				elif(limit==1 and dt[4]==0 and dt[5]==0 and dt[6]==0 and dt[7]==0):
					False;
				else:
					ans += dfs(pos-1,(mod+index*hash[pos-1])%dMod,dt2,0);
	if(limit==0):
		dp[pos][mod] = ans;
	return ans;

print dfs(lenID,0,dt,1);