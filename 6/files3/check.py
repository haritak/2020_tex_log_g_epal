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

a1 = a*len("garbage\n")
a2 = a*len("garbage")

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

if i == a1 or i==a2:
    print "Check 4: passed - Το νούμερο των χαρακτήρων είναι σωστό"
    if i == a2:
        print "BONUS!!! Το πλήθος των χαρακτήρων αγνοεί τις αλλαγές γραμμών!"
else:
    print "Check 4: FAILED - Το νούμερο των χαρακτήρων είναι λάθος"


print "End of checks!"

