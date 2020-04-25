#!/bin/python3

import math
import os
import random
import re
import sys
'''
def check(X,val):
    global combos
    if val == X:
        print('success')
        combos+=1
        return 1
    else:
        return 0

def getCombos(X, N,prev_total=0,start_index=0):
    print('previous total: {}'.format(prev_total))
    if start_index == X - 1 or prev_total > X:
        return
    global combos
    total = 0
    print("SI: {}".format(start_index))
    possibleList = [i for i in range(1, X)]
    print(possibleList)
    ptr_val = possibleList[start_index]
    print("PTR  val: {}".format(ptr_val))
    status=check(X, pow(ptr_val, N))
    if status:
        return 1
    total += pow(ptr_val, N)
    print('total updated to at start: {0}'.format(total))
    for j in range(start_index+1,X):
        print('checking now with {} against {}'.format(ptr_val,possibleList[j]))
        print('total is : {}'.format(total))
        for i in range(j, X):
            print("current iter: {0} , {1}".format(i, possibleList[i]))
            if pow(possibleList[i], N) > X or i == X - 1 or total > X:
                print('flag 1')
                return 2
            if possibleList[i] == ptr_val or possibleList[i] == 0:
                print('flag 2')
                # total+=pow(possibleList[i],N)
                # print('total updated to: {0}'.format(total))
                # check(X,total)
                continue
            total += pow(possibleList[i], N)
            status=check(X, total)
            if status:
                return 1
            print('total updated to: {0}'.format(total))
            if total > X:
                total -= pow(possibleList[i], N)
                print('total updated to after return 2: {0}'.format(total))
                return total
            #series-> 6,7,
            #trigger 6, 36 check, +next iter ie. 7, total=36+49=85, into iter 8 where +8>X, back to iter 7, total back to 85.
            total= total + prev_total
            status=check(X, total)
            result = getCombos(X, N, total, i)
            if result == 2:
                total-=pow(possibleList[i],N)
                print('total updated to after return: {0}'.format(total))
                break



# Complete the powerSum function below.
def powerSum(X, N):
    possibleList=[i for i in range(1,X)]
    for i in possibleList:
        if pow(i,N)<=X:
            print("Next Triggered: {}".format(i))
    getCombos(X,N,0,0)

combos = 0
ptr = 0
print(powerSum(100, 3))
print(combos)
'''


def totnum(X,N,num=1):
    print('func called with params: {} , {} , {}'.format(X,N,num))
    if(pow(num,N)<X):
        return (totnum(X,N,num+1)+totnum(X-pow(num,N),N,num+1))
    elif(pow(num,N)==X):
        return 1
    else:
        return 0


print(totnum(100,2))