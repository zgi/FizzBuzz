# -*- coding: utf-8 -*-
run = True

while run == True:
    try:
        stevilo = int(raw_input("Vnesi število med 1 in 100\n"))
        if stevilo <= 100 and stevilo >= 1:
            for x in range(1, stevilo + 1):
                if x % 3 == 0 and x % 5 == 0:
                    print "fizzBuzz"
                elif x % 5 == 0:
                    print "buzz"
                elif x % 3 == 0:
                    print "fizz"
                else:
                    print x
            run = False
        else:
            print "Število je premajhno ali preveliko."

    except ValueError:
        print "Kar si vpisal, ni število..."