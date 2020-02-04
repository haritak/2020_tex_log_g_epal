#!/usr/bin/python2
# -*- coding: utf-8 -*-

from solution import solution

print "Before checking, make sure file days.txt is removed!"
print "Use the rm days.txt command to remove it"
print "Press enter to continue"
raw_input()

i = solution(1)
print "Check 1: passed - No syntax errors"


if i == 1:
    print "Check 2: passed - Η επιστρεφόμενη τιμή είναι σωστή"
else:
    print "Check 2: FAILED - Η επιστρεφόμενη τιμή είναι λάθος"

f = open("numbers.txt")
counter = 0
f3counter = 0
lines = ["one", "two", "three"]
for i in f:
    if i!=lines[counter]+"\n":
        print "Check 3: FAILED - λάθος περιεχόμενα στο numbers.txt"
        f3counter+=1
    counter+=1

if f3counter==0:
        print "Check 3: passed - σωστά περιεχόμενα στο numbers.txt"
    
f.close()
f=open("days.txt")
l1 = f.readline()
if l1=="Mon\n":
    print "Check 4: passed - σωστή πρώτη μέρα στο days.txt"
else:
    print "Check 4: FAILED - λάθος πρώτη μέρα στο days.txt"

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i in range(2,7):
    lines = solution(i)
    if lines!=i:
        print "Check : FAILED - λάθος επιστρεφόμενη τιμή"
    else:
        print "Check : passed - σωστή επιστρεφόμενη τιμή"
    f = open("days.txt")
    line_counter = 0
    for line in f:
        if line != days[line_counter]+'\n':
           print "Check : FAILED - λάθος περιεχόμενα στο days.txt"
        line_counter+=1

print "End of checks!"

