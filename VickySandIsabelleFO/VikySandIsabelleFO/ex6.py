#-------------------------------------------------------------------------------
# Name:      Exercise 6
#
# Purpose:   define function is_numeric
#
# Author:    David Viljoen
#
# Date:      04-10-2019
#
# CreatedBy: Isabelle and Chengjiaqi Sun
#-------------------------------------------------------------------------------
def main():
    """main()"""

def is_numeric(test_string):
    """Given a letter a, b, c return x, y, z respectively
    """
    str(test_string)

    if (str(test_string))[0] == '-':
        test_string = (str(test_string)) [1:]

        if (str(test_string)).isdigit ():
            return True
        else:
            return False


    else:
        if (str(test_string)).isdigit():
            return True
        else:
            return False

#postive, negative whole numbers true
#else return false


if __name__ == '__main__':
    main()
