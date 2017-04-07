#!/usr/bin/python


debug = 0

if debug == 1:
    limit = [8,20]
    n = 3
    p = [[2,10],[10,12],[8,30],[1,5]]
    #n = 1
    # p = [[8,30]] 
    print limit
    print n
    print p

def isIn(arr):

    if arr[0] > limit[1] or arr[1] < limit[0] or \
    arr[1] == 0:
        return False
    else:
        return True

def overlapNum():

    count = 0
    maxN = 0
    minN = 10001

    global p
    global limit
    if debug !=1: 
        limit = []
        p = []
        n = 0
        i = 0

        s = raw_input().split(" ")
        limit = map(int,s)     
        n = input()

        while i<n:
            s = raw_input().split(" ")
            p.append([int(s[0]),int(s[1])])
            i = i + 1
        if n == 0:
            print 0
            print 0
            return

    p = filter(isIn,p)  #Filtered out those not in limit scale

    #add 0,1 to the start and end time
    l = []
    for i in range(len(p)):
        l.append((p[i][0],0))
        l.append((p[i][1],1))

    #sort
    l = sorted(l)

    #count 0 and 1
    if limit[1] == 0 or len(l) == 0:
        print 0
        print 0
        return

    if l[0][0] > limit[0] or l[-1][0] < limit[1]:
        minN = 0

    for k in l:
        if k[1] == 0:
            count = count + 1
            maxN = max(maxN,count)
            if minN != 0:
                minN = count
        else: #k[1] == 1
            if k[0] < limit[1]:
                count = count -1
        if minN != 0:
            minN = min(minN,count)

    if minN >= 10001:
        print 0
    else:
        print minN
    print maxN
    return

if __name__ == "__main__":
    overlapNum()
