#!/usr/bin/python2
# -*- coding: utf-8 -*-

from solution import solution

P =  [1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 8, 8, 9, 12, 21, 21, 23, 32, 34, 42, 65, 123, 123, 213, 213, 312, 321, 321, 432, 765, 876, 3213, 6765, 678213]
i = solution(P)

print "Check 1: passed - No syntax errors"

if i == 1270763454298898280154629117241974324345669963428659200000:
    print "Check 2: passed - Σωστό γινόμενο"
else:
    print "Check 2: FAILED - Λάθος γινόμενο"

i = solution([])
if i == 1:
    print "Check 3: passed - Σωστό γινόμενο"
else:
    print "Check 3: FAILED - Λάθος γινόμενο"

i = solution([1,2,3,4,5,6,7,8,9])
if i == 362880:
    print "Check 4: passed - Σωστό γινόμενο"
else:
    print "Check 4: FAILED - Λάθος γινόμενο"
