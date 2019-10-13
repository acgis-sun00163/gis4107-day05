#-------------------------------------------------------------------------------
# Name:       test_ex2.py
#
# Purpose:    Test ex2 module.
#
# Author:     David Viljoen
#
# Date:       04-10-2019
#
# CreatedBy:  Isabelle and Chengjiaqi Sun
#-------------------------------------------------------------------------------


import ex2
reload(ex2)

def main():
    """main()"""
    xmin = 2
    ymin= 1
    xmax = 7
    ymax= 9

    expected = True
    x=2
    y=2
    actual = ex2.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, expected, actual)

    expected = False
    x = 1
    y = 10
    actual = ex2.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, expected, actual)

def compare_expected_and_actual(x, y, expected, actual):
    if expected == actual:
        print 'PASSED:  For x, y= {}, {}'.format(x, y)
    else:
        fmt = 'FAILED: For x,y = {}, {}\nExpected: {}\nActual:   {}'
        print fmt.format(x, y, expected, actual)


main()