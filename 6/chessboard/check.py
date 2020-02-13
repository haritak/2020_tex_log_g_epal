#!/usr/bin/python2
# -*- coding: utf-8 -*-

from solution import solution

solution()
print "Check 1: passed - No syntax errors"

f = open("chessboard.txt", "w")
f.write("_________________\n")
for i in range(8):
    f.write(". . . . . . . . .\n")
f.write("-----------------\n")
f.close()
solution()

f = open("chessboard.txt", "r")
lineno = 0
errors = 0
for line in f:
    corrent_line = "";
    if lineno==0:
        corrent_line = "_________________\n"
    elif lineno==9:
        corrent_line = "-----------------\n"
    elif lineno%2==0:
        corrent_line = ". .X. .X. .X. .X.\n"
    elif lineno%2==1:
        corrent_line = ".X. .X. .X. .X. .\n"
    if line==corrent_line:
        print "Line number ", lineno, "is ok."
    else:
        print "Line number ", lineno, "is DESTROYED!"
        errors+=1

    lineno+=1

if errors == 0:
    print "Check 2: passed - Η σκακιέρα είναι τέλεια!"
else:
    print "Check 2: FAILED - Η σκακιέρα έχει προβλήματα!"


f.close()
f = open("chessboard.txt", "w")
f.write("_________________\n")
for i in range(8):
    f.write("| | | | | | | | |\n")
f.write("-----------------\n")
f.close()
print "End of checks!"

