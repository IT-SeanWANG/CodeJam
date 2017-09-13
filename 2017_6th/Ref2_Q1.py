# python 3.1 win64,  LouisLiu, Aug.22, 2017
import sys

def mycheck(K, M, Clist):
    L = len(Clist)
    I = K -1
    while L > 2:
        if L == 3:
            Clist.pop(I)
            print(Clist[0], Clist[1])
            sys.exit()
        Clist.pop(I)
        L -= 1
        I -= 1
        if M % L > 0:
            M1 = M % L
        else:
            M1 = L
        if I + M1 <= L - 1:
            I += M1
        else:
            I = I + M1 - L

if __name__ == '__main__':
    myinput = input().split(' ')
    N = int(myinput[0])
    K = int(myinput[1])
    M = int(myinput[2])
    Childlist = [i for i in range(1,N + 1)]
    L1 = len(Childlist) - 1
    if M % L1 == 0:
        if K + L1 > Childlist[-1]:
            K = K + L1 - Childlist[-1]
        else:
            K = K + L1
    else:
        if K + M % L1 > Childlist[-1]:
            K = K + M % L1 - Childlist[-1]
        else:
            K = K + M % L1
    mycheck(K, M, Childlist)
