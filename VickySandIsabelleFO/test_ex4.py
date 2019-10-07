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

import ex4
reload(ex4)

def main():
    """main()"""

    #Assignment statement 1
    expected = 5
    myvar = 1
    actual = ex4.mod_my_var(myvar)
    compare_expected_and_actual(myvar, expected, actual)

    #Assignment statement 2
    expected = 2
    myvar = 3
    actual = ex4.mod_my_var(myvar)
    compare_expected_and_actual(myvar, expected, actual)

    #assignment statement 3
    expected = 4
    myvar = 2
    actual = ex4.mod_my_var(myvar)
    compare_expected_and_actual(myvar, expected, actual)

    #assignment statement 4
    expected = 10
    myvar = 12
    actual = ex4.mod_my_var(myvar)
    compare_expected_and_actual(myvar, expected, actual)

def compare_expected_and_actual(myvar, expected, actual):
    if expected == actual:
        print 'PASSED:  For myvar = {}'.format(myvar)
    else:
        fmt = 'FAILED: For myvar = {}\nExpected: {}\nActual:   {}'
        print fmt.format(myvar, expected, actual)

if __name__ == '__main__':
    main()
