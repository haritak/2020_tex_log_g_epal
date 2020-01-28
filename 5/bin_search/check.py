#!/usr/bin/python2
# -*- coding: utf-8 -*-

from solution import solution

P =  [0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 8, 8, 9, 12, 21, 21, 23, 32, 34, 42, 65, 123, 123, 213, 213, 312, 321, 321, 432, 765, 876, 3213, 6765, 678213]
i = solution(P, 2)

print "Check 1: passed - No syntax errors"
i = solution(P, 2)
if i == 5:
    print "Check 2: passed - Ψάξιμο τιμής που υπάρχει"
else:
    print "Check 2: FAILED - Ψάξιμο τιμής που υπάρχει, λάθος αποτέλεσμα. Θα έπρεπε να είναι 5 και είναι ", i

i = solution(P, 34)
if i == 21:
    print "Check 3: passed - Ψάξιμο τιμής που υπάρχει"
else:
    print "Check 3: FAILED - Ψάξιμο τιμής που υπάρχει, λάθος αποτέλεσμα. Θα έπρεπε να είναι 21 και είναι ", i

i = solution(P, P[-1])
if i == len(P)-1:
    print "Check 4: passed - Ψάξιμο ακραίας τιμής που υπάρχει"
else:
    print "Check 4: FAILED - Ψάξιμο ακραίας τιμής που υπάρχει, λάθος αποτέλεσμα. Θα έπρεπε να είναι ", len(P)-1," και είναι ", i

i = solution(P, P[0])
if i == 0:
    print "Check 5: passed - Ψάξιμο ακραίας τιμής που υπάρχει"
else:
    print "Check 5: FAILED - Ψάξιμο ακραίας τιμής που υπάρχει, λάθος αποτέλεσμα. Θα έπρεπε να είναι ", 0," και είναι ", i

i = solution(P, -12002)
if i == -1:
    print "Check 6: passed - Ψάξιμο τιμής που δεν υπάρχει"
else:
    print "Check 5: FAILED - Ψάξιμο τιμής δεν που υπάρχει, λάθος αποτέλεσμα. Θα έπρεπε να είναι ", -1," και είναι ", i
