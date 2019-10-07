#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Isabelle
#
# Created:     01-10-2019
# Copyright:   (c) Isabelle 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import ex2
reload(ex2)

def main():
    """main()"""
    xmin = 1
    ymin= 1
    xmax = 5
    ymax= 5

    expected = True
    x=2
    y=2
    actual = ex2.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, expected, actual)

    expected = False
    x = 1
    y = 2
    actual = ex2.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, expected, actual)

def compare_expected_and_actual(x, y, expected, actual):
    if expected == actual:
        print 'PASSED:  For x, y= {}, {}'.format(x, y)
    else:
        fmt = 'FAILED: For x,y = {}, {}\nExpected: {}\nActual:   {}'
        print fmt.format(x, y, expected, actual)


main()
