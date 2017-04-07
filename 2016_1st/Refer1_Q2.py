#coding:utf8
import sys, time
import itertools

#3~W 分别对应 3到16
def tran(cards = ""):
    tmp = []

    tmp = [0 for i in range(17)]

    for i in cards:
        if i == "S":
            tmp[10] += 1
        elif i == "J":
            tmp[11] += 1
        elif i == "Q":
            tmp[12] += 1
        elif i == "K":
            tmp[13] += 1
        elif i == "A":
            tmp[14] += 1
        elif i == "2":
            tmp[15] += 1
        elif i == "W":
            tmp[16] += 1
        else:
            tmp[int(i)] += 1

    return tmp
	
#统计目前手里的牌的数量
def getNumOfCards(cards = []):
    nums = 0

    for i in cards:
        nums += i

    return nums

#获取相同数字的牌的组合
def getSameCards(cards = [], num = 0):

    result = []
	
    #判断剩余的牌的数量够不够
    if getNumOfCards(cards) < num:
        return []

    for i in range(3, 17):
        if cards[i] >= num:
            tmp = [i for j in range(num)]
            result.append(tmp)

    return result
	
#获取三带一，三带二
def getThreeAdd(cards = []):

    tmp = []
    three = getSameCards(cards , 3)

    for ele in three:
        index = ele[0] 
        value = cards[index]
        cards[index] = 0
        
        one = getSameCards(cards, 1)

        for e in one:
            tmp.append(ele + e)
        two = getSameCards(cards, 2)

        for e in two:
            tmp.append(ele + e)
        cards[index] += value

    return tmp

#获取所有的单顺
def getSigle(cards = []):
    tmp = []
    #单顺最少5张,最多3~A 共12张
    for nums in range(5 , 13):
        if getNumOfCards(cards) < nums:
            break
        for i in range(3, 14 - nums + 2):
            t = [ cards[j] for j in range(i, i + nums)]

            if 0 not in t:
                t1 = [j for j in range(i, i + nums)]
                tmp.append(t1)
    return tmp
	
#获取所有双顺, 即连对
def getDoubleShun(cards = []):
    tmp = []
    #获取所有的对子
    twoCard = getSameCards(cards , 2)

    #最多的连对是8连对 3 ~ A, 但是一共才17张牌

    for nums in range(3 , 9):
        if getNumOfCards(cards) < nums * 2:
            break
        if len(twoCard) <  nums:
            break
			
        #i代表起始从3开始, 最多到Q结束
        for i in range(3, 12):
            t = []
            for j in range(i, i + nums):
                t1 = [j, j]
                if t1 not in twoCard: 
                    break
                t += t1
            if len(t) == nums * 2:
                tmp.append(t)
    return tmp
	
#获取所有的飞机
def getPlane(cards = []):

    #飞机至少是2连 最多5连
    tmp = []
    three = getSameCards(cards, 3)
    for nums in range(2 , 6):
        if getNumOfCards(cards) < nums * 3:
            break
        if len(three) <  nums:
            break
       
        for i in range(3, 13):
            t = []
            for j in range(i, i + nums):
                t1 = [j, j, j]
                if t1 not in three: 
                    break
                t += t1
            if len(t) == nums * 3:
                tmp.append(t)
    return tmp

#飞机带翅膀
def getPlaneFly(cards = []):
    tmp = []
    planes = getPlane(cards)

    for plane in planes:
        length = len(plane) / 3
        t = cards[:]
        for e in plane:
            t[e] -= 1
        oneFly = getSameCards(t, 1)
        twoFly = getSameCards(t, 2)

        if len(oneFly) < length:
            continue
	
		#生成列表a,所有长度为n的子集
        sigle = list(itertools.permutations(oneFly, length))
        for i in sigle: 
            tmp.append(plane + [i[0][0], i[1][0]])

        for i in twoFly:
            tmp.append(plane + i)
    return tmp

#四带二
def getFourTwo(cards = []):
    tmp = []
    fourCards = getSameCards(cards, 4)
    for f in fourCards:
        index = f[0]
        cards[index] -= 4
        one = getSameCards(cards, 1)
        for i in range(len(one) - 1 ):
            for j in range( i + 1, len(one)):
                tmp.append(f + [one[i][0], one[j][0]])

        two = getSameCards(cards, 2)
        for i in two:
            tmp.append(f + i)

        cards[index] += 4
    return tmp

def retran(num):
    if num > 2 and num < 10:
        return str(num)

    elif num == 10:
        return "S"
    elif num == 11:
        return "J"
    elif num == 12:
        return "Q"
    elif num == 13:
        return "K"
    elif num == 14:
        return "A"
    elif num == 15:
        return "2"
    elif num == 16:
        return "W"
		
#从cards中移除player出的牌
def removeChar(cards, player):
	s = list(cards)
	for i in player:
            if  retran(i) in s:
                s.remove(retran(i))
	
	return "".join(s)

min = 17
def PlayCard(cards = "", count = 0):
    
    global min
    tmp = {}
    
    funs = (getFourTwo, getPlaneFly , getPlane, getDoubleShun, getSigle, getThreeAdd)
    if  count >  min:
        return (17, [])
    if len(cards) == 0:
        if count <= min:
            min = count

        return (0, [])
    else:
        
        c = tran(cards)
        for index ,fun in enumerate(funs): 
            ret = fun(c)
            for i in ret:				
                new_cards = removeChar(cards, i)
                n, des = PlayCard(new_cards, count + 1)
                if n == 17:
                    continue
                if tmp.get(n + 1, 0) == 0:
                    tmp[n + 1] = []
                if des != []:
                    for tt in des:
                        tt.append(i)
                        tmp[n + 1].append(tt)
                else:
                    tmp[n + 1].append([i,])
        #先出相同的
        for j in [4, 3, 2, 1]:
            ret = getSameCards(c, j)
            for i in ret:
                new_cards = removeChar(cards, i)
                n, des = PlayCard(new_cards, count + 1)
                if n == 17:
                    continue
                #print "n = %d, ret = %s" % (n, str(des))
                if tmp.get(n + 1, 0) == 0:
                    tmp[n + 1] = []

                if des != []:
                    for tt in des:
                        tt.append(i)
                        tmp[n + 1].append(tt)
                else:
                
                    tmp[n + 1].append([i,])
        list_key = sorted(tmp.keys())
        if list_key == []:
            return 17, []

    
        return (list_key[0], tmp[list_key[0]])

def testPlayCard(listx):
    #输入手牌，示例有空格

    #print "Input cards with space:"
    #input = raw_input().split(' ')
    input = listx.split(' ')

    if len(input) != 17:
        print "error input"
        exit()

    n , m = PlayCard(input)

    allway = []
    # winter for path error
    path = []
    for e in m:
        path = []
        for ch in e:
            la = [retran(i) for i in sorted(ch) ]
            ss = "".join(la)
            path.append(ss)
        allway.append(" ".join(sorted(path)))

    output = set(tuple(allway))

    #输出结果

    print "Output:"

    print len(path)

    for e in output:
        print e


def test999():
    list1 = ["3 3 3 4 4 4 5 5 6 7 8 9 S J Q K A",
"3 4 5 6 7 8 9 J Q K A 2 2 2 2 W W",
"3 3 4 4 5 5 6 6 7 7 8 8 9 9 2 2 2",
"3 3 3 4 4 4 5 5 5 6 7 8 S S S 2 2",
"3 3 5 5 6 7 8 9 J J Q K K A 2 W W",
"5 5 5 6 6 6 7 7 7 8 8 8 J Q K A W",
"3 3 4 4 5 5 8 8 8 9 9 9 S S S W W",
"3 4 5 5 5 6 7 8 9 S J Q K A A A A"]
    #print list1
    i=1
    for x in list1:
        #cardcase = list(x)
        print "======= CASE", i, " begin: ", x
        newcase = testPlayCard(x)
        #PlayCard(newcase)
        print "------- CASE", i, " end."
        i=i+1
test999()
