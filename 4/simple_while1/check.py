#!/usr/bin/python2
# -*- coding: utf-8 -*-

from solution import solution

l = solution()
print "Check 1: passed - No syntax errors"

l2 = []
x = 0
z = 1000
while x<=z: #Προσθέστε εδώ την σωστή συνθήκη.
    l2.append( (x,z) )
    x+=1
    z-=1

if l2 == l:
    print "Check 2: passed - Σωστός πίνακας"
else:
    print "Check 2: FAILED - Λάθος πίνακας! Προσπάθησε ξανά!"

