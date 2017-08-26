# --coding: utf-8--
import math


def polysum(n, s):
    """
    n: (int, positive) number of sides in a regular polygon
    s: (int or float, positive) length of each side
    
    returns: (float) area + perimeter^2  (rounded to 4 decimal places)
    """
    area = (0.25 * n * s**2) / math.tan(math.pi/n)
    perimeter = n * s
    return round(area + perimeter ** 2, 4)
