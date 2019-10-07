#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Isabelle
#
# Created:     04-10-2019
# Copyright:   (c) Isabelle 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    """main()"""

def mod_my_var(myvar):
    """Given a letter a, b, c return x, y, z respectively
    """
    if myvar % 2:
        if myvar ** 3 != 27:
            myvar += 4           # Assignment statement 1
        else:
            myvar /= 1.5         # Assignment statement 2
    else:
        if myvar <= 10:
            myvar *= 2           # Assignment statement 3
        else:
            myvar -= 2           # Assignment statement 4
    return myvar

#! means is not equal to
# myvar % 2  means myvar/x = remainder 1


if __name__ == '__main__':
    main()
