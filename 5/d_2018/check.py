#!/usr/bin/python2
# -*- coding: utf-8 -*-

from solution import solution


d2_MO, d3_THER, d3_POL, d4_MAX_TEMP, d4_POL = solution()

print d2_MO
print d3_THER
print d3_POL
print d4_MAX_TEMP
print d4_POL

print "Congrats! Your solution passes check 1: No syntax errors!"
if d2_MO == sum([32.0, 31.0, 30.0, 29.0, 28.0, 27.0, 27.0, 26.0, 25.0])/len([32.0, 31.0, 30.0, 29.0, 28.0, 27.0, 27.0, 26.0, 25.0]):
    print "Congrats! Your solution passes check 2: MO is ok!"
else:
    print "Ooops! MO is not ok!"
if d3_THER == [32.0, 31.0, 30.0, 29.0, 28.0, 27.0, 27.0, 26.0, 25.0]:
    print "Congrats! Your solution passes check 3: THER is ok!"
else:
    print "Ooops! THER is not OK!"
if d3_POL == ['Ierapetra', 'Moires', 'Heraklio', 'Athens', 'Rethimno', 'Larisa', 'Agios Nikolaos', 'Chania', 'Patra']:
    print "Congrats! Your solution passes check 4: POL is ok!"
else:
    print "Ooops! POL is not OK!"
if d4_MAX_TEMP == 32.0:
    print "Congrats! Your solution passes check 5: MAX_TEMP is ok!"
else:
    print "Ooops! MAX_TEMP is not OK!"
if d4_POL == ['Ierapetra']:
    print "Congrats! Your solution passes check 6: POL for d4 is ok!"
else:
    print "Ooops! POL for d4 is not OK!"

