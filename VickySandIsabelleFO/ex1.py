#-------------------------------------------------------------------------------
# Name:    example.py
#
# Purpose: Contains some_func function that converts a, b, or c into x, y, or z
#
# Author:  David Viljoen
#
# Created: 29/09/2019
#-------------------------------------------------------------------------------

def main():
    """main()"""

def get_feature_type(feature_code):
    """Given a letter a, b, c return x, y, z respectively
    """


    if feature_code == 1:
        return 'POINT'

    elif feature_code == 2:
        return 'LINE'

    elif feature_code == 3:
        return 'POLYGON'

    else:
        return None


main()


