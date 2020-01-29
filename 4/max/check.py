#!/usr/bin/python2
# -*- coding: utf-8 -*-

from solution import solution
import random
import sys

P =  [0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 8, 8, 9, 12, 21, 21, 23, 32, 34, 42, 65, 123, 123, 213, 213, 312, 321, 321, 432, 765, 876, 3213, 6765, 678213]
i = solution(P)

print "Check 1: passed - No syntax errors"

if i == max(P):
    print "Check 2: passed - Σωστή μέγιστη τιμή"
else:
    print "Check 2: FAILED - Λάθος μέγιστη τιμή"

for j in range(1, 10):
    L = random.sample(range(1,1000), 100)
    i = solution(L)
    if i == max(L):
        print "Check",j+2,": passed - Σωστή μέγιστη τιμή"
    else:
        print "Check",j+2,": FAILED - Λάθος μέγιστη τιμή"
        sys.exit()


