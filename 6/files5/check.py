#!/usr/bin/python2
# -*- coding: utf-8 -*-

from solution import solution
from random import randint

filename = "sample.txt"
f=open(filename, "w")
for i in range(40):
    line = "O" * 80 + "\n"
    f.write(line)

a = f.tell()
a = randint(0, a)
f.seek(a, 0)
f.write("o")
f.close()

i = solution(filename)
print "Check 1: passed - No syntax errors"

if i != None:
    print "Check 2: passed - Η συνάρτηση επιστρέφει κάτι."
else:
    print "Check 2: FAILED - Η συνάρτηση ΔΕΝ επιστρέφει κάτι."

if isinstance(i, int):
    print "Check 3: passed - Η συνάρτηση επιστρέφει ακέραιο."
else:
    print "Check 3: FAILED - Η συνάρτηση ΔΕΝ επιστρέφει ακέραιο."

if i == a:
    print "Check 4: passed - Η συνάρτηση επιστρέφει τον σωστό ακέραιο."
    f = open(filename)
    f.seek(i)
    a = f.read(1)
    if a == "X":
        print "Check 5: passed - Στο αρχείο μπήκε το Χ στην σωστή θέση!"
    else:
        print "Check 5: FAILED - Δεν βρήκα το X στην σωστή θέση..."
else:
    print "Check 4: FAILED - Η συνάρτηση ΔΕΝ επιστρέφει τον σωστό ακέραιο."




print "End of checks!"

