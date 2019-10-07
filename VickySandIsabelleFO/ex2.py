#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Isabelle
#
# Created:     01-10-2019
# Copyright:   (c) Isabelle 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def is_point_in_box(x, y, xmin, ymin, xmax, ymax):
    """Given a letter a, b, c return x, y, z respectively"""

    if (xmin < x < xmax) and (ymin < y < ymax):
        return True

    else:
        return False


