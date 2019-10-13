#-------------------------------------------------------------------------------
# Name:       test_ex1.py
#
# Purpose:    Test ex1 module.
#
# Author:     David Viljoen
#
# Date:       04-10-2019
#
# CreatedBy:  Isabelle and Chengjiaqi Sun
#-------------------------------------------------------------------------------

import ex1
reload(ex1)

def main():
    """main()"""
    expected = 'POINT'
    feature_code = 5
    actual = ex1.get_feature_type(feature_code)
    compare_expected_and_actual(feature_code, expected, actual)

    expected = 'POLYLINE'
    feature_code = 3
    actual = ex1.get_feature_type(feature_code)
    compare_expected_and_actual(feature_code, expected, actual)

    expected = 'POLYGON'
    feature_code = 2
    actual = ex1.get_feature_type(feature_code)
    compare_expected_and_actual(feature_code, expected, actual)

    expected = None
    feature_code = 9
    actual = ex1.get_feature_type(feature_code)
    compare_expected_and_actual(feature_code, expected, actual)



def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()






