# -*- coding: utf-8 -*-
def fizzbuzz(stevilo):
    for x in range(1, stevilo):
        if x % 3 == 0 and x % 5 == 0:
            print "fizzbuzz"
        elif x % 5 == 0:
            print "buzz"
        elif x % 3 == 0:
            print "fizz"
        else:
            print x


def vpis_stevila():
    try:
        stevilo = int(raw_input("Vnesi število med 1 in 100\n"))
        if stevilo <= 100 and stevilo >= 1:
            fizzbuzz(stevilo)
        else:
            print "Število je premajhno ali preveliko."
            vpis_stevila()
    except ValueError:
        print "Kar si vpisal, ni število..."
        vpis_stevila()


vpis_stevila()
