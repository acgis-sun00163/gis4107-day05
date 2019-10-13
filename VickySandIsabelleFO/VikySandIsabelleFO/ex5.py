#-------------------------------------------------------------------------------
# Name:      Exercise 5
#
# Purpose:   define function is_divisible
#
# Author:    David Viljoen
#
# Date:      04-10-2019
#
# CreatedBy: Isabelle and Chengjiaqi Sun
#-------------------------------------------------------------------------------
def main():
    """main()"""

def is_divisible(numerator, denominator):
    """Given a letter a, b, c return x, y, z respectively
    """
    if  (str(numerator)).isdigit() and (str(denominator)).isdigit():

        if (type(numerator) == int) and (type(denominator) == int):
            if int(numerator) % int(denominator):
                return False
            else:
                return True
        else:
            if (int(numerator) % int(denominator)):
                return False
            else:
                return True

    else:
        return False






if __name__ == '__main__':
    main()