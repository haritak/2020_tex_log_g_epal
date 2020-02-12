#!/usr/bin/python2
# -*- coding: utf-8 -*-

from os import path
from solved import solution


filename = "test.file.txt"

solution(filename)
print "Check 1: passed - No syntax errors"



if path.exists(filename):
    print "Check 2: passed - Το αρχείο δημιουργήθηκε"
else:
    print "Check 2: FAILED - Το αρχείο δεν δημιουργήθηκε"

f = open(filename)
data = f.read()
if len(data)==3:
    print "Check 3: passed - Το αρχείο έχει το σωστό μέγεθος"
else:
    print "Check 3: FAILED - Το αρχείο δεν έχει το σωστό μέγεθος"

if data=="123":
    print "Check 4: passed - Το αρχείο έχει σωστά περιεχόμενα"
else:
    print "Check 4: FAILED - Το αρχείο δεν έχει σωστά περιεχόμενα (123)"
    

print "End of checks!"

