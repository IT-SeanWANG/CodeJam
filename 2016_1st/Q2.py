#! /usr/bin/env python
# coding: utf-8
# python version: 2.7.9
__author__ = 'Sean WANG'

import os
import sys
import time
import copy
import itertools
import logging

# used to trace control
# level=logging.ERROR to close trace
logging.basicConfig(format='[%(levelname)s]:%(asctime)s:%(filename)s:%(lineno)d:%(message)s',
                    datefmt='%Y:%m:%d-%H:%M:%S',level=logging.ERROR)

# input cards dictionary
dic_in = {'3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'S': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, '2': 16,
          'W': 17}

# output cards dictionary
dic_out = {3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
           10: 'S', 11: 'J', 12: 'Q', 13: 'K', 14: 'A', 16: '2',
           17: 'W'}

# convert string to list
def strtolist(str):
    tmp_list = []
    for item in str.split():
        tmp_list.append(dic_in[item])
    tmp_list.sort()
    return tmp_list

# list0 = [3, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list0 = []

# # # get 17 cards input
"""
while not 17 == len(list0):
    valid_flg = 1
    str = raw_input();
    # check input valid
    for item in str.split():
        if not dic_in.has_key(item):
            print item,'is not a valid input'
            valid_flg = 0
            del list0[:]
            break
    # check input card's quantity is valid
    for item in dic_in.keys():
        if 'W' == item and str.split().count(item) > 2:
            valid_flg = 0
            del list0[:]
            print 'the card - %s amount is more than 2 , input again:' % item
            break
        elif str.split().count(item) > 4:
            valid_flg = 0
            del list0[:]
            print 'the card - %s amount is more than 4 , input again:' % item
            break

    if valid_flg == 1:
        list0 = strtolist(str)
        if 17 != len(list0):
            print 'all cards number is not 17, input again:'
"""
# # # previous process cards
# in: list_in = [3, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# out:
# list1 = [3,4,5,6,7,8,9,10,11,12,13,14]
# list2 = [3,4,5]
# list3 = [3,4]
# list4 = []
def get_four_list(list_in):
    list1 = list(set(list_in))
    list1.sort()
    tem_list = copy.copy(list_in)
    for item in list1:
        tem_list.remove(item)
    list2 = list(set(tem_list))
    list2.sort()
    for item in list2:
        tem_list.remove(item)
    list3 = list(set(tem_list))
    list3.sort()
    for item in list3:
        tem_list.remove(item)

    list4 = list(set(tem_list))
    list4.sort()

    return list1, list2, list3, list4

# # # get all bomb
def getallbomb(card_list):
    tmp_list = get_four_list(card_list)[3]
    if 0 == len(tmp_list):
        return 0
    return tmp_list

# # # get all san tiao
def getallthreecards(card_list):
    tmp_list = get_four_list(card_list)[2]
    if 0 == len(tmp_list):
        return 0

    return tmp_list

# # # get all combinations that item nb >= begin
def getcombinations(begin, card_list):
    tmp_list = []
    for i in range(begin, len(card_list) + 1):
        iter = itertools.combinations(card_list, i)
        for item in list(iter):
            tmp = list(item)
            tmp.sort()
            tmp_list.append(tmp)
    return tmp_list

# # # whether the list is sanshun
# the input should has been sorted
def is_sanshun(card_list=[]):
    length = len(set(card_list))
    if length == 0:
        return 0
    if length == (card_list[-1] - card_list[0] + 1) and length > 1:
        return 1
    else:
        return 0

# # # whether it is a shunzi
# the input should has been sorted
def is_shunzi(card_list=[]):
    length = len(set(card_list))
    if length == 0:
        return 0
    if 0 == length:
        return 0
    if length == (card_list[-1] - card_list[0] + 1) and length > 4:
        return 1
    else:
        return 0

# # # whether it is a sanshun
# the input should has been sorted
def is_shuangshun(card_list=[]):
    length = len(set(card_list))
    if length == 0:
        return 0
    if length == (card_list[-1] - card_list[0] + 1) and length > 2:
        return 1
    else:
        return 0

# # # get all sanshun
def getallsanshun(card_list):
    tmp_list = getallthreecards(card_list)
    tmp = []
    if 0 == tmp_list:
        return 0
    for item in getcombinations(2, tmp_list):
        if is_sanshun(item):
            tmp.append(item)
    if len(tmp) == 0:
        return 0
    return tmp

# # # get all duizi
# in: [2,3,3,4,4,5,6,8]
# out: [3,4,6]
def getalltwocards(card_list):
    tmp_list = get_four_list(card_list)[1]
    if 0 == len(tmp_list):
        return 0
    return tmp_list

# # # get all shuangshun from card list
# in: [4,4,5,5,6,6,7,7,8,8]
# out: [[4,5,6],[6,7,8],[4,5,6,7]]
def getallshuangshun(card_list):
    tmp_list = getalltwocards(card_list)
    tmp = []
    # print 'tmp_list=',tmp_list
    if 0 == tmp_list:
        return 0
    for item in getcombinations(3, tmp_list):
        if is_shuangshun(item):
            tmp.append(item)
    if len(tmp) == 0:
        return 0
    return tmp


# # # get all danzhi in card list
# in: [4,5,6,6,6,8,9,9]
# out: [4,5,6,8,9]
def getallonecards(card_list):
    tmp_list = get_four_list(card_list)[0]
    if 0 == len(tmp_list):
        return 0
    return tmp_list

# # # get all shunzi from card list
# in: [3,4,5,6,7,8]
# out: [[3,4,5,6,7],[4,5,6,7,8],[3,4,5,6,7,8]]
def getallshunzi(card_list):
    tmp_list = getallonecards(card_list)
    tmp = []
    if 0 == tmp_list:
        return 0
    for item in getcombinations(5, tmp_list):
        if is_shunzi(item):
            tmp.append(item)
    if len(tmp) == 0:
        return 0
    return tmp

# # # function: convert to [value] * size = [value,value,value]
def fullfillcards(size, card_list):
    tmp_list = []
    for item in card_list:
        tmp_size = size
        while tmp_size != 0:
            tmp_list.append(item)
            tmp_size -= 1
    return tmp_list

# # # get all types besides 'dandui' and 'danzhi' and 'santiao'
splitlen2sanshunflg = 1
splitbombtoduiflg = 1
lenbomb4flg = 0
def getalltypes(card_list):
    global splitlen2sanshunflg,\
           splitbombtoduiflg,\
           lenbomb4flg

    empty_flg = 0
    tmp_dic = {}
    types_list = []

    tmp_list = getallbomb(card_list)
    if 0 != tmp_list:
        if len(tmp_list) == 4 and 3 == tmp_list[-1] - tmp_list[0]:
            splitbombtoduiflg = 0
        if len(tmp_list) == 4 and 0 == getallsanshun(card_list):
            lenbomb4flg = 1

        tmp_dic['bomb'] = tmp_list
        for item in tmp_list:
            types_list.append([item for x in range(4)])
            empty_flg += 1
        # split duizi [3 3 3 3 2 W W 5 6 7 8 9 S J Q K A]
        # [3 3 3 3 2 W W 5 5 5 7 7 7 9 9 9 S]
        # 3 3 3 3 2 W W 4 4 6 6 8 8 S S Q Q
        tmp_card_list = removecards(card_list, fullfillcards(4,tmp_list)) #[item]
        if not getallshuangshun(tmp_card_list) and not getallsanshun(tmp_card_list) \
                and not getallshunzi(tmp_card_list):
            tmp_lv = getalltwocards(tmp_card_list)
            # print tmp_card_list
            if 0 != tmp_lv:
                for l_item in tmp_lv:
                    types_list.append([l_item])
            ''' 3 3 3 4 4 4 5 5 5 2 W 7 7 9 9 9 9
                3 3 3 3 5 5 5 6 6 6 7 7 7 9 9 9 9
            buchaisantiao wrong'''

            tmpl_list = getallthreecards(fullfillcards(4,tmp_list)) #[item]
            if 0 != tmpl_list:
                tmp_dic['santiao'] = tmpl_list
                for item in tmpl_list:
                    if splitbombtoduiflg:
                        types_list.append([item for x in range(3)])
                        types_list.append([item for x in range(2)])
                empty_flg += 1

    tmp_list = getallsanshun(card_list)
    if 0 != tmp_list:
        for tmp_l in tmp_list:
            if len(tmp_l) > 2:
                splitlen2sanshunflg = 0
                break

        tmp_dic['sanshun'] = tmp_list
        for item in tmp_list:
            if 4 == len(item):
                tmp_card_list = removecards(card_list, fullfillcards(3, item))
                if is_shunzi(tmp_card_list):
                    for l_item in tmp_card_list:
                        types_list.append([l_item])

                tmp_lv = getalltwocards(tmp_card_list)
                if 0 != tmp_lv:
                    for l_item in tmp_lv:
                        types_list.append([l_item])

            if 3 == len(item):
                tmp_card_list = removecards(card_list, fullfillcards(3, item))
                if not getallshuangshun(tmp_card_list) and not getallshunzi(tmp_card_list) \
                                                            and not getallbomb(tmp_card_list):
                    tmp_lv = getallthreecards(tmp_card_list)
                    if 0 != tmp_lv:
                        for l_item in tmp_lv:
                            types_list.append([l_item,l_item])

                # split shuangshun
                if is_shuangshun(tmp_card_list) and 4 == len_shun(tmp_card_list):
                    tmp_lv = getalltwocards(tmp_card_list)
                    if 0 != tmp_lv:
                        for l_item in tmp_lv:
                            types_list.append([l_item,l_item])
                # split duizi [3 3 3 4 4 4 5 5 5 2 W 7 7 9 9 9 9]
                if len(card_list) <= 13:
                    tmp_lv = getalltwocards(tmp_card_list)
                    if 0 != tmp_lv:
                        for l_item in tmp_lv:
                            types_list.append([l_item])

            if 2 == len(item) and splitlen2sanshunflg:
                tmp_lv = getallthreecards(fullfillcards(3, item))
                if 0 != tmp_lv:
                    for l_item in tmp_lv:
                        types_list.append([l_item,l_item,l_item])

                tmp_card_list = removecards(card_list, fullfillcards(3, item))
                if not getallshuangshun(tmp_card_list) and not getallshunzi(tmp_card_list) \
                                   and not getallsanshun(tmp_card_list) and not getallbomb(tmp_card_list):
                    tmp_lv = getalltwocards(tmp_card_list)
                    if 0 != tmp_lv:
                        for l_item in tmp_lv:
                            types_list.append([l_item])

            types_list.append(fullfillcards(3, item))
        empty_flg += 1

    tmp_list = getallshuangshun(card_list)
    if 0 != tmp_list:
        tmp_dic['shuangshun'] = tmp_list
        for item in tmp_list:
            types_list.append(fullfillcards(2, item))
        empty_flg += 1

    tmp_list = getallshunzi(card_list)
    if 0 != tmp_list:
        tmp_dic['shunzi'] = tmp_list
        for item in tmp_list:
            types_list.append(item)
        empty_flg += 1

        # split shunzi
        tmp_card_list = card_list
        if not getallshuangshun(tmp_card_list) and not getallsanshun(tmp_card_list) \
        and not getallbomb(tmp_card_list):
            tmp_lv = getalltwocards(tmp_card_list)
            # print tmp_card_list
            if 0 != tmp_lv:
                # print tmp_lv
                for l_item in tmp_lv:
                    types_list.append([l_item, l_item])
            tmp_list = getallthreecards(tmp_card_list)
            if 0 != tmp_list:
                for item in tmp_list:
                    types_list.append([item for x in range(3)])
                empty_flg += 1

    '''
    tmp_list = getalltwocards(card_list)
    if 0 != tmp_list:
        tmp_dic['duizi'] = tmp_list
        for item in tmp_list:
            types_list.append([item, item])
        empty_flg += 1
    '''

    if 0 == empty_flg:
        return 0
    else:
        return types_list

# remove cards from card list
def removecards(card_list, out_list):
    tmp_list = copy.copy(card_list)
    if type(out_list) != list:
        out_list = [out_list]
    for item in out_list:
        if item in tmp_list:
            tmp_list.remove(item)
        else:
            print 'an error should debug no include item = ', item
            return tmp_list
    return tmp_list

# # # find out all out cards types in card list
# in: [1,2,3,3,4,4,5,6,6,6,7]
# out: all classified card combination
# two global variables, used in the 'digui' function
result = []
A = []
def search(card_list):
    cards_hand = copy.copy(card_list)
    tmp_list = getalltypes(cards_hand)
    C = []
    if tmp_list == 0:
        B = copy.copy(A)

        tmp_v = getallthreecards(cards_hand)
        if 0 != tmp_v:
            for item in tmp_v:
                tmp_l = [item, item,item]
                B.append(tmp_l)
                cards_hand = removecards(cards_hand, tmp_l)

        tmp_v = getalltwocards(cards_hand)
        if 0 != tmp_v:
            for item in tmp_v:
                tmp_l = [item, item]
                B.append(tmp_l)
                cards_hand = removecards(cards_hand, tmp_l)

        tmp_v = getallonecards(cards_hand)
        if 0 != tmp_v:
            for item in tmp_v:
                tmp_l = [item]
                B.append(tmp_l)

        result.append(B)
        del A[:]
    else:
        for item in tmp_list:
            for l_item in C:
                A.append(l_item)
            A.append(item)
            tmp_list2 = removecards(cards_hand, item)
            C = copy.copy(A[:-1])
            search(tmp_list2)

# # #: remove the copied item from the list
# in: [[[6,6],[1]],[[2,2],[4]],[[4],[2,2]],[[6],[2]],[[4],[5,5]],[[1],[6,6]]]
# out: [[[2,2],[4]],[[6],[2]],[[4],[5,5]],[[1],[6,6]]]
def removerepeat(result_list):
    tmp_list = copy.copy(result_list)
    for item in tmp_list:
        if list == type(item):
            for ll_item in item:
                ll_item.sort()
        item.sort()
    tmp_result = []
    for item in tmp_list:
        if item in tmp_result:
            continue
        else:
            tmp_result.append(item)
    return tmp_result

# # # get type of the input card list
# in: [3,4,5,6,7]
# out: 'shunzi'
def get_card_type(card_list):
    length = len(card_list)
    kinds_nb = len(set(card_list))
    cardtype = 'other'

    # 1
    if 1 == length and kinds_nb == length:
        cardtype = 'danzhi'

    # 2
    if length >= 5 and kinds_nb == length:
        cardtype = 'shunzi'

    # 3
    if length == 4 and kinds_nb == 1:
        cardtype = 'bomb'

    # 4
    if length == 3 and kinds_nb == 1:
        cardtype = 'santiao'

    # 5
    if length == 2 and kinds_nb == 1:
        cardtype = 'duizi'

    # 6
    if length >= 6 and length / kinds_nb == 2:
        cardtype = 'shuangshun'

    # 7
    if length >= 6 and length / kinds_nb == 3:
        cardtype = 'sanshun'

    return cardtype

# compute lenth of shunzi, shuangshun, sanshun
# in: shunzi or shuangshun or sanshun
# out: length
def len_shun(card_list):
    kinds_nb = len(set(card_list))
    return kinds_nb

# get type count of card list that after classify
# input: [[3, 3, 3], [4, 4], [5, 5, 5, 5], [8, 9, 10, 11, 12], [10], [13], [14]]
def getdetailinfo(card_list):
    count_danzhi = 0
    danzhi_list = []
    count_shunzi = 0
    shunzi_lsit = []
    count_duizi = 0
    duizi_list = []
    count_shuangshun = 0
    shuangshun_list = []
    count_santiao = 0
    santiao_list = []
    count_sanshun = 0
    sanshun_list = []
    count_bomb = 0
    bomb_list = []

    for item in card_list:
        l_item = get_card_type(item)
        if 'danzhi' == l_item:
            count_danzhi += 1
            danzhi_list.append(item)
        if 'shunzi' == l_item:
            count_shunzi += 1
            shunzi_lsit.append(item)
        if 'duizi' == l_item:
            count_duizi += 1
            duizi_list.append(item)
        if 'shuangshun' == l_item:
            count_shuangshun += 1
            shuangshun_list.append(item)
        if 'santiao' == l_item:
            count_santiao += 1
            santiao_list.append(item)
        if 'sanshun' == l_item:
            count_sanshun += 1
            sanshun_list.append(item)
        if 'bomb' == l_item:
            count_bomb += 1
            bomb_list.append(item)
    tmp_list = [count_danzhi, danzhi_list, \
                count_shunzi, shunzi_lsit, \
                count_duizi, duizi_list, \
                count_shuangshun, shuangshun_list, \
                count_santiao, santiao_list, \
                count_sanshun, sanshun_list, \
                count_bomb, bomb_list]
    return tmp_list

# # # combine santiao, sanshun, bomb with duizi or danzhi
# st_list = santiao_list
# sanh_list = sanshun_list
# bom_list = bomb_list
# dan_list = danzhi_list
# dui_list = duizi_list
# output: all possible combine
def get_combined(st_list=[], sanh_list=[], bom_list=[], dan_list=[], dui_list=[],shuans_list=[]):
    l_result = []

    #combine santiao
    for item in [[x, y] for x in st_list for y in dan_list + dui_list]:
        if 0 != len(item):
            l_result.append(item)

    # combine sanshun
    for item in sanh_list:
        l_len = len_shun(item)

        # 1 duizi
        if 2 == l_len:
            for l_item in [[x, y] for x in [item] for y in dui_list]:
                if 0 != len(l_item):
                    l_result.append(l_item)

        # 1 duizi + 1 danzhi
        # 1 santiao
        if 3 == l_len:
            tmp_vl = [[x, y] for x in dan_list for y in dui_list]
            for l_item in [[x, y] for x in [item] for y in tmp_vl]:
                tmp_item = [l_item[0], l_item[1][0], l_item[1][1]]
                if 0 != len(tmp_item):
                    l_result.append(tmp_item)

            if 0 != shuans_list:
                tmp_sslist = []
                for ll_item in shuans_list:
                    if 3 == len_shun(ll_item):
                        tmp_sslist.append(ll_item)

                for l_item in [[x, y] for x in [item] for y in tmp_sslist]:
                    if 0 != len(l_item):
                        l_result.append(l_item)
        # if 4 == len
        # 2 danzhi + 1 duizi
        # 2 duizi
        # 1 santiao + 1 danzhi
        # for when there is 4==len(sanshun), duizi--->danzhi
        # so no need to care about duizi + danzhi

        # full danzhi and full duizi
        tmp_list1 = list(itertools.combinations(dan_list, l_len))
        tmp_list1 += list(itertools.combinations(dui_list, l_len))
        for l_item in [[x, y] for x in [item] for y in tmp_list1]:
            tmp_item = [l_item[0]]
            for i in range(0, l_len):
                tmp_item.append(l_item[1][i])
            if 0 != len(tmp_item):
                l_result.append(tmp_item)

    # combine bomb:
    tmp_list1 = list(itertools.combinations(dan_list, 2))
    tmp_list1 += list(itertools.combinations(dui_list, 2))
    for item in [[x, y] for x in bom_list for y in tmp_list1]:
        tmp_item = [item[0], item[1][0], item[1][1]]
        if 0 != len(tmp_item):
            l_result.append(tmp_item)

    for l_item in [[x, y] for x in bom_list for y in dui_list]:
        if 0 != len(l_item):
            l_result.append(l_item)

    l_result = removerepeat(l_result)

    return l_result


# # # get all out cards methods
# two global variables used to 'digui' function
out_result = []
X = []
def out_cards(card_list):
    C = []
    info_list = getdetailinfo(card_list)
    cards_hand_list = copy.copy(card_list)
    combine_list = get_combined(info_list[9], info_list[11], info_list[13], info_list[1], info_list[5], info_list[7])
    # print 'combine_list', combine_list
    if 0 == len(combine_list):
        B = copy.copy(X)
        for re_item in info_list[1] + info_list[3] + info_list[5] + \
                info_list[7] + info_list[9] + info_list[11] + info_list[13]:
            B.append(re_item)
        out_result.append(B)
        del X[:]
    else:
        for tmp_item in combine_list:
            for l_item in C:
                X.append(l_item)
            X.append(tmp_item)
            # print 'cards_hand_list,tmp_item',cards_hand_list,tmp_item
            tmp_list2 = removecards(cards_hand_list, tmp_item)
            C = copy.copy(X[:-1])
            out_cards(tmp_list2)

# # # compute min shoushu form out_card_list
def findoutminshoushu_card(out_card_list):
    min_shoushu = 17
    l_cardlist = []

    for item in out_card_list:

        if len(item) > min_shoushu:
            continue
        elif len(item) < min_shoushu:
            del l_cardlist[:]
            l_cardlist.append(item)
            min_shoushu = len(item)
        else:
            l_cardlist.append(item)
    return min_shoushu, l_cardlist


# # # get get result: min shoushu and detail out cards
# invoke fundamental functions
def get_final_result(card_list):
    global result, out_result, lenbomb4flg
    del result[:]
    tmp_time = time.time() #######
    search(card_list)
    removerepeat(result)###

    # # begin to process type like: [4 4 4 4 6 6 6 6 8 8 8 8 J J J J 3]
    if lenbomb4flg :
        tmp_result = []
        for lt_item in result:
            tmp_len = 0
            for lo_item in lt_item:
                if len(lo_item) == 4:
                    tmp_len += 1
            if tmp_len < 2:
                continue
            else:
                tmp_result.append(lt_item)
        result = tmp_result
    # # end

    logging.info('result length = %s, used time = %s', len(result),time.time() - tmp_time)
    min_nb = 17
    result_list = []

    for item in result:
        del out_result[:]
        out_cards(item)
        # print 'out_result length = ', len(out_result),time.time() - tmp_time #######
        out_result = removerepeat(out_result)
        item_result = findoutminshoushu_card(out_result)
        if item_result[0] > min_nb:
            continue
        elif item_result[0] < min_nb:
            del result_list[:]
            result_list += item_result[1]
            min_nb = item_result[0]
        else:
            result_list += item_result[1]
    result_list = removerepeat(result_list)
    return min_nb, result_list

# # # sort the string as nb
# in: '544666'
# out: '666445'
def sortstring(str_in):
    l_str = ''
    tmp_str = str_in[0]
    for i in range(len(str_in)):
        if tmp_str != str_in[i]:
            tmp_str = str_in[i]
            l_str += ' '
        l_str += tmp_str

    l = ([(x, len(x)) for x in l_str.split()])
    l.sort(key=lambda k: k[1], reverse=True)
    l_str = ''
    for item in l:
        l_str += item[0]
    return l_str

# # # convert result list to output
# input: [[[3, 3, 3], [8, 8]], [[4, 4, 4, 5, 5, 5, 6, 6, 6], [8], [9, 9]]]
# output: 444555666899 33388
def convert2output(in_list):
    out_str = ''
    for item in in_list:
        for l_item in item:
            if type(l_item) == list:
                for tmp_m in l_item:
                    out_str += dic_out[int(tmp_m)]
            else:
                out_str += dic_out[int(l_item)]
        out_str += ' '
    l = ([(sortstring(x), len(x)) for x in out_str.split()])
    l.sort(key=lambda k: k[1], reverse=True)
    tmp_str = ''
    for item in l:
        tmp_str += item[0]
        tmp_str += ' '

    return tmp_str


# # # the interface function to get input and print output
def PlayCard(input_cards=[]):
    # print 'compute the result . . .'
    tmplist = get_final_result(input_cards)
    last_list = []
    # output the min 'shoushu' number
    print tmplist[0]
    # output all out card schemes
    for item in tmplist[1]:
        tmp_list = convert2output(item)
        if tmp_list not in last_list:
            print tmp_list.strip()
            last_list.append(tmp_list)

#
aa = time.time()  # add to debug
# main function
#PlayCard(list0)
#logging.info("used time = %s", time.time() - aa)  # add to debug

# print getalltypes([4, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 11, 11, 11, 11, 3])
# print getalltypes([4,4, 4, 4, 6, 6, 6, 6, 5, 7, 3, 3, 9, 8, 8, 9, 1,0])

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
        newcase = strtolist(x)
        PlayCard(newcase)
        print "------- CASE", i, " end."
        i=i+1
test999()