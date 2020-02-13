#!/usr/bin/python2
# -*- coding: utf-8 -*-

from random import randint
from solution import solution


somewords = ["sadsaDWQ", "asdsawqewqeqas", "sadqwewqdasd", "asdsadqw", "asdsawqq",
        "sfgwreyyj", "dsfqtewvcxv", "ewdsafsvsaxzc"]

#create a random file
words = []
filename = "test.file.txt"
f = open(filename, "w")
for i in range(10):
    a = randint(0, len(somewords)-1)
    f.write(somewords[a])
    words.append(somewords[a])
    f.write(" ")
    if i%10==0:
        f.write("\n")
f.close()

i = solution(filename)
print "Check 1: passed - No syntax errors"

if i != None:
    print "Check 2: passed - Η συνάρτηση επιστρέφει κάτι."
else:
    print "Check 2: FAILED - Η συνάρτηση δεν επιστρέφει τίποτα."

if isinstance(i, list):
    print "Check 3: passed - Η συνάρτηση επιστρέφει μία λίστα."
else:
    print "Check 3: FAILED - Η συνάρτηση δεν επιστρέφει λίστα."

words_sorted = words[:].sort()

if words == i or words_sorted == i:
    print "Check 4: passed - Η λίστα είναι σωστή!"
    if words_sorted == i:
        print "BONUS!!!! Η λίστα είναι ταξινομημένη!"
else:
    print "Check 4: FAILED - Η λίστα είναι λάθος"


print "End of checks!"

