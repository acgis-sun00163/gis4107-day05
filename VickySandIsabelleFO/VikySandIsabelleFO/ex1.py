#-------------------------------------------------------------------------------
# Name:      Exercise 1
#
# Purpose:   Contains some_func function that converts a, b, or c into x, y, or z
#
# Author:    David Viljoen
#
# Date:      04-10-2019
#
# CreatedBy: Isabelle and Chengjiaqi Sun
#-------------------------------------------------------------------------------

def main():
    """main()"""

def get_feature_type (feature_code):
    """Given a letter a, b, c return x, y, z respectively
    """

    if feature_code ==1:
        return 'POINT'

    elif feature_code ==2:
        return 'POLYLINE'

    elif feature_code ==3:
        return 'POLYGON'
    else:
        return 'NONE'

if __name__ == '__main__':
    main()
