# python 3.1 win64,  LouisLiu, Aug.25, 2017
import sys, datetime

leapyear = []
validlist = []
totallist = []
sub10 = []
sub8 = []
daylist = []
monlist = []
ylist = []
datelist = []
xlist = [10, 9, 8, 7, 6, 5, 4, 3, 2] * 2
Slist = []

def find_all_index(arr,item):
    return [i for i,a in enumerate(arr) if a==item]

def checkdate(y, m, d):
    try:
        datetime.date(y, m, d)
        dd = '0' + str(d)
        mm = '0' + str(m)
        yyyy = '000' + str(y)
        datelist.append(dd[-2:] + mm[-2:] + yyyy[-4:])
        return True
    except:
        return False

def subtotal(f):
    for s in datelist:
        res = 0
        #DD = list(s)
        DD = list(map(int, s))
        for i in range(8):
            res += xlist[i] * DD[i]
        sub8.append(res % 19)
    v = 0
    for m in sub8:
        for n in sub10:
            H = (m + n) % 19
            if H <= 9 and H == f:
                v += 1
            elif 19 - H == f:
                v += 1
    totallist.append(v)
    myprint(f, totallist)

def myprint(flag, Plist):
    if flag == 'B':
        IDsub = 1
        for i in Plist:
            IDsub *= i
        print(IDsub)
        sys.exit()
    else:
        print(sum(Plist))
        sys.exit()

def mycheck(Clist):
    A = Clist[-1]
    indexlist = find_all_index(Clist[:-1], 'B')
    indexlist.sort()
    list1 = Clist[:-1]
    L = len(indexlist)
    if A == 'B':
        if min(indexlist) >= 8:
            for i in range(len(indexlist)):
                validlist.append(10)
            myprint(A, validlist)
        if L <= 2 and max(indexlist) == 1:
            tmplist = Clist[2:-1]
            month = 10*tmplist[0] + tmplist[1]
            year = 1000*tmplist[2] + 100*tmplist[3] + 10*tmplist[4] + tmplist[5]
            if indexlist == [0, 1]:
                if month == 2:
                    if  year in leapyear:
                        validlist.append(29)
                    else:
                        validlist.append(28)
                else:
                    if month in [1,3,5,7,8,10,12]:
                        validlist.append(31)
                    else:
                        validlist.append(30)
            elif indexlist == [0]:
                if month == 2:
                    n = int(Clist[1])
                    if n == 0:
                        validlist.append(2)
                    elif n == 9:
                        if year in leapyear:
                            validlist.append(3)
                        else:
                            validlist.append(2)
                    else:
                        validlist.append(3)
                else:
                    validlist.append(4)
            else:
                n = int(Clist[0])
                if n == 0:
                    validlist.append(9)
                elif n == 1:
                    validlist.append(10)
                elif n == 2:
                    if year in leapyear:
                        validlist.append(10)
                    else:
                        if month == 2:
                            validlist.append(9)
                        else:
                            validlist.append(10)
                elif n == 3:
                    if month in [1, 3, 5, 7, 8, 10, 12]:
                        validlist.append(2)
            myprint(A, validlist)
        if L >=8 and indexlist[:8] == [0, 1, 2, 3, 4, 5, 6, 7]:
            validlist.append((365*9999+len(leapyear)))
            if L > 8:
                for i in range(len(indexlist[8:])):
                    validlist.append(10)
            myprint(A, validlist)

    # date related part for both
    tmpindex = indexlist[:]
    for i in indexlist:
        if i >= 8:
            validlist.append(10)
            tmpindex.remove(i)
    for i in tmpindex:
        if list1[i] == 'B':
            list1.pop(i)
            if i == 0:
                list1.insert(i, [0, 1, 2, 3])
            elif i == 1:
                list1.insert(i, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            elif i == 2:
                list1.insert(i, [0, 1])
            elif i == 3:
                list1.insert(i, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            elif i == 4:
                list1.insert(i, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            elif i == 5:
                list1.insert(i, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            elif i == 6:
                list1.insert(i, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            elif i == 7:
                list1.insert(i, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    sub = 0
    if 0 in tmpindex and 1 in tmpindex:
        [daylist.append(10 * a + b) for a in list1[0] for b in list1[1]]
    elif 0 in tmpindex and 1 not in tmpindex:
        [daylist.append(10 * a + list1[1]) for a in list1[0]]
    elif 0 not in tmpindex and 1 in tmpindex:
        [daylist.append(10 * list1[0] + b) for b in list1[1]]
    else:
        daylist.append(10 * list1[0] + list1[1])
    if len(daylist) > 1:
        [daylist.remove(d) for d in daylist if d not in range(1, 32)]
    if 2 in tmpindex and 3 in tmpindex:
        [monlist.append(10 * a + b) for a in list1[2] for b in list1[3]]
    elif 2 in tmpindex and 3 not in tmpindex:
        [monlist.append(10 * a + list1[3]) for a in list1[2]]
    elif 2 not in tmpindex and 3 in tmpindex:
        [monlist.append(10 * list1[2] + b) for b in list1[3]]
    else:
        monlist.append(10 * list1[2] + list1[3])
    if len(monlist) > 1:
        [monlist.remove(m) for m in monlist if m not in range(1, 13)]
    if 4 in tmpindex and 5 in tmpindex and 6 in tmpindex and 7 in tmpindex:
        [ylist.append(1000 * a + 100 * b + 10 * c + d) for a in list1[4] for b in list1[5] for c in list1[6] for d in
         list1[7]]
    elif 4 in tmpindex and 5 in tmpindex and 6 in tmpindex and 7 not in tmpindex:
        [ylist.append(1000 * a + 100 * b + 10 * c + list1[7]) for a in list1[4] for b in list1[5] for c in list1[6]]
    elif 4 in tmpindex and 5 in tmpindex and 6 not in tmpindex and 7 in tmpindex:
        [ylist.append(1000 * a + 100 * b + 10 * list1[6] + d) for a in list1[4] for b in list1[5] for d in list1[7]]
    elif 4 in tmpindex and 5 not in tmpindex and 6 in tmpindex and 7 in tmpindex:
        [ylist.append(1000 * a + 100 * list1[5] + 10 * c + d) for a in list1[4] for c in list1[6] for d in list1[7]]
    elif 4 not in tmpindex and 5 in tmpindex and 6 in tmpindex and 7 in tmpindex:
        [ylist.append(1000 * list1[4] + 100 * b + 10 * c + d) for b in list1[5] for c in list1[6] for d in list1[7]]
    elif 4 in tmpindex and 5 in tmpindex and 6 not in tmpindex and 7 not in tmpindex:
        [ylist.append(1000 * a + 100 * b + 10 * list1[6] + list1[7]) for a in list1[4] for b in list1[5]]
    elif 4 in tmpindex and 5 not in tmpindex and 6 in tmpindex and 7 not in tmpindex:
        [ylist.append(1000 * a + 100 * list1[5] + 10 * c + list1[7]) for a in list1[4] for c in list1[6]]
    elif 4 in tmpindex and 5 not in tmpindex and 6 not in tmpindex and 7 in tmpindex:
        [ylist.append(1000 * a + 100 * list1[5] + 10 * list1[6] + d) for a in list1[4] for d in list1[7]]
    elif 4 not in tmpindex and 5 in tmpindex and 6 in tmpindex and 7 not in tmpindex:
        [ylist.append(1000 * list1[4] + 100 * b + 10 * c + list1[7]) for b in list1[5] for c in list1[6]]
    elif 4 not in tmpindex and 5 in tmpindex and 6 not in tmpindex and 7 in tmpindex:
        [ylist.append(1000 * list1[4] + 100 * b + 10 * list1[6] + d) for b in list1[5] for c in list1[6]]
    elif 4 not in tmpindex and 5 not in tmpindex and 6 in tmpindex and 7 in tmpindex:
        [ylist.append(1000 * list1[4] + 100 * list1[5] + 10 * c + d) for c in list1[6] for d in list1[7]]
    elif 4 in tmpindex and 5 not in tmpindex and 6 not in tmpindex and 7 not in tmpindex:
        [ylist.append(1000 * a + 100 * list1[5] + 10 * list1[6] + list1[7]) for a in list1[4]]
    elif 4 not in tmpindex and 5 in tmpindex and 6 not in tmpindex and 7 not in tmpindex:
        [ylist.append(1000 * list1[4] + 100 * b + 10 * list1[6] + list1[7]) for b in list1[5]]
    elif 4 not in tmpindex and 5 not in tmpindex and 6 in tmpindex and 7 not in tmpindex:
        [ylist.append(1000 * list1[4] + 100 * list1[5] + 10 * c + list1[7]) for c in list1[6]]
    elif 4 not in tmpindex and 5 not in tmpindex and 6 not in tmpindex and 7 in tmpindex:
        [ylist.append(1000 * list1[4] + 100 * list1[5] + 10 * list1[6] + d) for d in list1[7]]
    else:
        ylist.append(1000 * list1[4] + 100 * list1[5] + 10 * list1[6] + list1[7])
    if len(ylist) > 1:
        [ylist.remove(y) for y in ylist if y == 0]
    if len(daylist) > 1 and len(monlist) > 1 and len(ylist) > 1:
        for day in daylist:
            for month in monlist:
                for year in ylist:
                    if checkdate(year, month, day):
                        sub += 1
    elif len(daylist) > 1 and len(monlist) > 1 and len(ylist) == 1:
        for day in daylist:
            for month in monlist:
                if checkdate(ylist[0], month, day):
                    sub += 1
    elif len(daylist) > 1 and len(monlist) == 1 and len(ylist) > 1:
        for day in daylist:
            for year in ylist:
                if checkdate(year, monlist[0], day):
                    sub += 1
    elif len(daylist) == 1 and len(monlist) > 1 and len(ylist) > 1:
        for month in monlist:
            for year in ylist:
                if checkdate(year, month, daylist[0]):
                    sub += 1
    elif len(daylist) > 1 and len(monlist) == 1 and len(ylist) == 1:
        for day in daylist:
            if checkdate(ylist[0], monlist[0], day):
                sub += 1
    elif len(daylist) == 1 and len(monlist) > 1 and len(ylist) == 1:
        for month in monlist:
            if checkdate(ylist[0], month, daylist[0]):
                sub += 1
    elif len(daylist) == 1 and len(monlist) == 1 and len(ylist) > 1:
        for year in ylist:
            if checkdate(year, monlist[0], daylist[0]):
                sub += 1
    else:
        checkdate(ylist[0], monlist[0], daylist[0])
    if sub > 1:
        validlist.append(sub)
    if A == 'B':
        myprint(A, validlist)

    # A is not  'B' case
    if A != 'B':
        Lz = list1[8:].count('B')
        if Lz == 0:
            res = 0
            for i in range(8, 18):
                res += xlist[i] * list1[i]
            sub10.append(res)
            subtotal(A)
        else:
            res1 = 0
            res11 = 0
            res2 = 0
            zlist = []
            inlist = [n for n in indexlist if n > 7]
            if Lz < 10:
                [zlist.append(i) for i in range(8, 18) if i not in inlist]
                for n in zlist:
                    res2 += xlist[n] * list1[n]
            if Lz == 1:
                for a in range(10):
                    res1 = xlist[inlist[0]] * a + res2
                    sub10.append(res1)
            elif Lz == 2:
                for a in range(10):
                    for b in range(10):
                        res1 = xlist[inlist[0]] * a + xlist[inlist[1]] * b + res2
                        sub10.append(res1)
            elif Lz == 3:
                for a in range(10):
                    for b in range(10):
                        for c in range(10):
                            res1 = xlist[inlist[0]] * a + xlist[inlist[1]] * b + xlist[inlist[2]] * c + res2
                            sub10.append(res1)
            elif Lz == 4:
                for a in range(10):
                    for b in range(10):
                        for c in range(10):
                            for d in range(10):
                                res1 = xlist[inlist[0]] * a + xlist[inlist[1]] * b + xlist[inlist[2]] * c + xlist[inlist[3]] * d + res2
                                sub10.append(res1)
            elif Lz == 5:
                for a in range(10):
                    for b in range(10):
                        for c in range(10):
                            for d in range(10):
                                for e in range(10):
                                    res1 = xlist[inlist[0]] * a + xlist[inlist[1]] * b + xlist[inlist[2]] * c + \
                                           xlist[inlist[3]] * d + xlist[inlist[4]] * e + res2
                                    sub10.append(res1)
            elif Lz == 6:
                L1 = []
                L2 = []
                for a in range(10):
                    for b in range(10):
                        for c in range(10):
                            for d in range(10):
                                for e in range(10):
                                    res1 = xlist[inlist[0]] * a + xlist[inlist[1]] * b + xlist[inlist[2]] * c + \
                                           xlist[inlist[3]] * d + xlist[inlist[4]] * e
                                    L1.append(res1)
                for f in range(10):
                    res11 =  xlist[inlist[5]] * f + res2
                    L2.append(res11)
                [sub10.append(m + n) for m in L1 for n in L2]
            elif Lz == 7: #new way
                L1 = []
                L2 = []
                for a in Slist[inlist[0]]:
                    for b in Slist[inlist[1]]:
                        for c in Slist[inlist[2]]:
                            for d in Slist[inlist[3]]:
                                for e in Slist[inlist[4]]:
                                    res1 = (a + b + c + d +e)% 19
                                    L1.append(res1)
                for f in Slist[inlist[5]]:
                    for g in Slist[inlist[6]]:
                        res11 = (f + g + res2) % 19
                        L2.append(res11)
                [sub10.append((m + n) % 19) for m in L1 for n in L2]

            elif Lz == 8:
                L1 = []
                L2 = []
                for a in range(10):
                    for b in range(10):
                        for c in range(10):
                            for d in range(10):
                                for e in range(10):
                                    res1 = xlist[inlist[0]] * a + xlist[inlist[1]] * b + xlist[inlist[2]] * c + \
                                           xlist[inlist[3]] * d + xlist[inlist[4]] * e
                                    L1.append(res1)
                for f in range(10):
                    for g in range(10):
                        for h in range(10):
                            res11 = xlist[inlist[5]] * f + xlist[inlist[6]] * g + xlist[inlist[7]] * h + res2
                            L2.append(res11)
                [sub10.append(m + n) for m in L1 for n in L2]
            elif Lz == 9:
                L1 = []
                L2 = []
                for a in range(10):
                    for b in range(10):
                        for c in range(10):
                            for d in range(10):
                                for e in range(10):
                                    res1 = xlist[inlist[0]] * a + xlist[inlist[1]] * b + xlist[inlist[2]] * c + \
                                           xlist[inlist[3]] * d + xlist[inlist[4]] * e
                                    L1.append(res1)
                for f in range(10):
                    for g in range(10):
                        for h in range(10):
                            for i in range(10):
                                res11 = xlist[inlist[5]] * f + xlist[inlist[6]] * g + xlist[inlist[7]] * h + \
                                        xlist[inlist[8]] * i + res2
                                L2.append(res11)
                [sub10.append(m + n) for m in L1 for n in L2]
            elif Lz == 10:
                L1 = []
                L2 = []
                for a in range(10):
                    for b in range(10):
                        for c in range(10):
                            for d in range(10):
                                for e in range(10):
                                    res1 = xlist[inlist[0]] * a + xlist[inlist[1]] * b + xlist[inlist[2]] * c + \
                                           xlist[inlist[3]] * d + xlist[inlist[4]] * e
                                    L1.append(res1)
                for f in range(10):
                    for g in range(10):
                        for h in range(10):
                            for i in range(10):
                                for j in range(10):
                                    res11 = xlist[inlist[5]] * f + xlist[inlist[6]] * g + xlist[inlist[7]] * h + \
                                            xlist[inlist[8]] * i + xlist[inlist[9]] * j
                                    L2.append(res11)
                [sub10.append(m + n) for m in L1 for n in L2]
        subtotal(A)

if __name__ == '__main__':
    IDlist = list(input())
    for i in range(len(IDlist)):
        if IDlist[i] != 'B':
            IDlist[i] = int(IDlist[i])
    if IDlist.count('B') == 0:
        print(1)
        sys.exit()
    if IDlist.count('B') == 1 and IDlist[-1] == 'B':
        print(1)
        sys.exit()
    for date in range(1, 10000):
        if (date % 4 == 0 and date % 100 != 0) or date % 400 == 0:
            leapyear.append(date)
    if IDlist.count('B') == 19:
        print((365*9999+len(leapyear))*10000000000)
        sys.exit()
    for i in range(9):
        Slist.append([xlist[i] * z % 19 for z in range(10)])
    Slist = Slist * 2
    mycheck(IDlist)
