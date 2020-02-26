#!/usr/bin/python2
# -*- coding: utf-8 -*-

from solved import solution
from random import randint

abc = "abcdefghijklmnopqrstuvwxyz"
total_vowels = 0
vowel_locations = []

filename = "sample.txt"
f=open(filename, "w")
for i in range(3):
    line = ""
    for cil in range(20):
        letter = abc[ randint(0, len(abc)-1) ]
        if letter in "aeiouy":
            total_vowels += 1
            vowel_locations.append( f.tell() )
        f.write(letter)
    f.write("\n")
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

if i == total_vowels:
    print "Check 4: passed - Η συνάρτηση επιστρέφει τον σωστό ακέραιο."
    f = open(filename)
    fails = 0
    for location in vowel_locations:
        f.seek( location )
        a = f.read(1)
        if a != "X":
            fails += 1
            print "Δεν μπήκε Χ στην θέση ", location
    if fails == 0:
        print "Check 5: passed - Στο αρχείο μπήκαν σωστά τα Χ!"
    else:
        print "Check 5: FAILED - Δεν βρήκα το X στην σωστή θέση..."
else:
    print "Check 4: FAILED - Η συνάρτηση ΔΕΝ επιστρέφει τον σωστό ακέραιο."




print "End of checks!"

