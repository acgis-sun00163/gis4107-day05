#-------------------------------------------------------------------------------
# Name:      Exercise 2
#
# Purpose:   define function is_point_in_box
#
# Author:    David Viljoen
#
# Date:      04-10-2019
#
# CreatedBy: Isabelle and Chengjiaqi Sun
#-------------------------------------------------------------------------------


"""Check the points inside the box or not"""


def is_point_in_box(x, y, xmin, ymin, xmax, ymax):
    """Given a letter a, b, c return x, y, z respectively"""

    if (xmin < x < xmax) and (ymin < y < ymax):
        return True

    else:
        return False