#!/usr/bin/python2
# -*- coding: utf-8 -*-

from solution import solution

P = solution()

print "Congrats! Your solution passes check 1: No syntax errors!"
if P == [0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 8, 8, 9, 12, 21, 21, 23, 32, 34, 42, 65, 123, 123, 213, 213, 312, 321, 321, 432, 765, 876, 3213, 6765, 678213]:
    print "Congrats! Your solution is correct!"
else:
    print "Ooops! Your solution fails check 2. It is NOT correct!"


