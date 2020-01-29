#!/usr/bin/python2
# -*- coding: utf-8 -*-

from solution import solution

P =  [0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 8, 8, 9, 12, 21, 21, 23, 32, 34, 42, 65, 123, 123, 213, 213, 312, 321, 321, 432, 765, 876, 3213, 6765, 678213]
i = solution(P)

print "Check 1: passed - No syntax errors"

if i == 692201:
    print "Check 2: passed - Σωστό άθροισμα"
else:
    print "Check 2: FAILED - Λάθος άθροισμα"

i = solution([])
if i == 0:
    print "Check 3: passed - Σωστό άθροισμα"
else:
    print "Check 3: FAILED - Λάθος άθροισμα"

i = solution([1,2,3,4,5,6,7,8,9])
if i == 45:
    print "Check 4: passed - Σωστό άθροισμα"
else:
    print "Check 4: FAILED - Λάθος άθροισμα"
