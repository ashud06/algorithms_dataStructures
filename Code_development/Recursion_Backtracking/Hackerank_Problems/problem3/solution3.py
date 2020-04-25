#!/bin/python3

import math
import os
import random
import re
import sys

def getSuperDigit(P):
    if len(P)==1:
        return P
    total=sum(int(val) for val in P)
    return getSuperDigit(str(total))


# Complete the superDigit function below.
def superDigit(n, k):
    digitTotal=sum(int(i) for i in n) * k
    return getSuperDigit(str(digitTotal))


if __name__ == '__main__':

    n = '9875'

    k = 4

    result = superDigit(n, k)

    print(result)
