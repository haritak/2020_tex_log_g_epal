#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Η συνάρτηση solution θα πρέπει να επιστρέφει με την παρακάτω σειρά:
# Δ2: Τον μέσο όρο των θερμοκρασιών
# Δ3: Τον ταξινομημένο ΤΗΕΡ
# Δ3: Τον αντίστοιχο POL
# Δ4: Την μέγιστη θερμοκρασία
# Δ4: Την λίστα με τις πόλεις με την μεγαλύτερη θερμοκρασία

def solution():
    arxeio = open("pth.txt", "r+")

    line_counter = 0
    for line in arxeio:
        print "Line number:", line_counter
        print "Line contents:", line
        line_counter += 1

solution()

