#! /usr/bin/env python
# coding: utf-8
# python version: 3.5.0
# author:Freda Li

import string
from numpy import *
import numpy as np

def DP(i, j, k):
    if (dp[i][j][k] != -1):
        return dp[i][j][k]
    if i>j:
        dp[i][j][k]=0
        return dp[i][j][k]
    dp[i][j][k]=DP(i+1,j,0)+np.square(1+k)
    for l in range (i+1,j+1):
        if  instr2[l]==instr2[i]:
            dp[i][j][k]=max(dp[i][j][k],DP(l,j,k+1)+DP(i+1,l-1,0))
    return dp[i][j][k]

#define variable
N=102
dp=-ones( (N, N,N), dtype = int)
instr2=zeros(N,dtype=str) 

#input string
instr=input("").split(",")
n=len(instr)

for i in range(n):
    instr2[i+1]=instr[i]

#output
result=DP(1,n,0)
print (result)

