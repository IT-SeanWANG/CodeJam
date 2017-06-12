#!/usr/bin/env python
import random
def remove_diamonds(L):

	N = len(L)
	res = [[[0]*N for _ in xrange(N)] for _ in xrange(N)]

	def dp(i,j,k):
		if i>j:
			return 0
		if res[i][j][k] != 0:
			return res[i][j][k]

		while(j>i and L[j] == L[j-1]):
			k += 1
			j -= 1
		res[i][j][k] = dp(i,j-1,0) + (1+k)**2

		for x in xrange(i,j):
			if L[x] == L[j]:
				res[i][j][k] = max(res[i][j][k], dp(i,x-1,0) + dp(x+1,j,k+1))

		return res[i][j][k]	

	return dp(0,N-1,0)	


if __name__ == '__main__':

	l = raw_input().split(',')

	res = remove_diamonds(l)
	print res
