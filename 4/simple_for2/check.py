#!/usr/bin/python2
# -*- coding: utf-8 -*-

from solution import solution

l = solution()
print "Check 1: passed - No syntax errors"

j1 = [i for i in range(100,49,-2)]
j2 = [i for i in range(49,10,-2)]
j3 = [i for i in range(10,0,-1)]
#print j1,j2,j3
j = j1+j2+j3
#print j

if l == j:
    print "Check 2: passed - Σωστός πίνακας"
else:
    print "Check 2: FAILED - Λάθος πίνακας! Προσπάθησε ξανά!"

