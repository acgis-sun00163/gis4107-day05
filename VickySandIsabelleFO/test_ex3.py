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

import ex3
reload(ex3)

def main():
    """main()"""
    x = 3
    m = 2
    b = 1

    expected = True
    y = 7
    actual = ex3.is_point_on_line(x, y, m, b)
    compare_expected_and_actual(y, expected, actual)

    expected = False
    y = 10
    actual = ex3.is_point_on_line(x, y, m, b)
    compare_expected_and_actual(y, expected, actual)

def compare_expected_and_actual(y, expected, actual):
    if expected == actual:
        print 'PASSED:  For y= {}'.format(y)
    else:
        fmt = 'FAILED: For y = {}\nExpected: {}\nActual:   {}'
        print fmt.format(y, expected, actual)

if __name__ == '__main__':
    main()
