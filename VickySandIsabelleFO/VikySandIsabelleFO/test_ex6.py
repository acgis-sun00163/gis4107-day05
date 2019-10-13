#-------------------------------------------------------------------------------
# Name:       test_ex6.py
#
# Purpose:    Test ex6 module.
#
# Author:     David Viljoen
#
# Date:       04-10-2019
#
# CreatedBy:  Isabelle and Chengjiaqi Sun
#-------------------------------------------------------------------------------

import ex6
reload(ex6)

def main():
    """main()"""
    expected = True
    test_string = '1'
    actual = is_numeric(test_string)
    compare_expected_and_actual(test_string, expected, actual)

    expected = True
    test_string = '-2'
    actual = is_numeric(test_string)
    compare_expected_and_actual(test_string, expected, actual)

    expected = False
    test_string = -2.0
    actual = is_numeric(test_string)
    compare_expected_and_actual(test_string, expected, actual)

    expected = False
    test_string = '2.0'
    actual = is_numeric(test_string)
    compare_expected_and_actual(test_string, expected, actual)

    expected = True
    test_string = -2
    actual = is_numeric(test_string)
    compare_expected_and_actual(test_string, expected, actual)

    expected = True
    test_string = 2
    actual = is_numeric(test_string)
    compare_expected_and_actual(test_string, expected, actual)

    expected = False
    test_string = 'test'
    actual = is_numeric(test_string)
    compare_expected_and_actual(test_string, expected, actual)

def compare_expected_and_actual(test_string, expected, actual):
    if expected == actual:
        print 'PASSED:  For test_string = {}'.format(test_string)
    else:
        fmt = 'FAILED: For test_string = {}\nExpected: {}\nActual:   {}'
        print fmt.format(test_string, expected, actual)

if __name__ == '__main__':
    main()




