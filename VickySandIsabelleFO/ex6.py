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
