#!/usr/bin/python2
# -*- coding: utf-8 -*-

from random import randint
from solution import solution

a = randint(0, 100)
filename = "test.file.txt"

f = open(filename, "w")
for i in range(a):
    f.write("garbage\n")

f.close()


i = solution(filename)
print "Check 1: passed - No syntax errors"

if i != None:
    print "Check 2: passed - Η συνάρτηση επιστρέφει κάτι."
else:
    print "Check 2: FAILED - Η συνάρτηση δεν επιστρέφει τίποτα."

if isinstance(i, int):
    print "Check 3: passed - Η συνάρτηση επιστρέφει έναν ακέραιο."
else:
    print "Check 3: FAILED - Η συνάρτηση δεν επιστρέφει ακέραιο."

if i == a:
    print "Check 4: passed - Το νούμερο των γραμμών είναι σωστό"
else:
    print "Check 4: FAILED - Το νούμερο των γραμμών είναι λάθος"


print "End of checks!"

