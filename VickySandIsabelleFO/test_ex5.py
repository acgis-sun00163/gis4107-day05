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

import ex5
reload(ex5)

def main():
    """main()"""

    expected = False
    numerator = '7'
    denominator = '2'
    actual = ex5.is_divisible(numerator, denominator)
    compare_expected_and_actual(numerator, denominator, expected, actual)

    expected = True
    numerator = 4
    denominator = 2
    actual = ex5.is_divisible(numerator, denominator)
    compare_expected_and_actual(numerator, denominator, expected, actual)

    expected = False
    numerator = -6
    denominator = -3
    actual = ex5.is_divisible(numerator, denominator)
    compare_expected_and_actual(numerator, denominator, expected, actual)

    expected = False
    numerator = -7
    denominator = -3
    actual = ex5.is_divisible(numerator, denominator)
    compare_expected_and_actual(numerator, denominator, expected, actual)



    expected = False
    numerator = '4.0'
    denominator = 2
    actual = ex5.is_divisible(numerator, denominator)
    compare_expected_and_actual(numerator, denominator, expected, actual)

    expected = True
    numerator = '4'
    denominator = 2
    actual = ex5.is_divisible(numerator, denominator)
    compare_expected_and_actual(numerator, denominator, expected, actual)


def compare_expected_and_actual(numerator, denominator, expected, actual):
    if expected == actual:
        print 'PASSED: For numerator, denominator = {}, {}'.format(numerator, denominator)
    else:
        fmt = 'FAILED: For numerator, denominator = {}, {}\nExpected: {}\nActual:   {}'
        print fmt.format(numerator, denominator, expected, actual)

if __name__ == '__main__':
    main()

