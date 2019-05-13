""" Lab 6: Sorting Algorithms
Chris Specht
Koichi Kodama
CPE 202-09
Spring 2019
Due Friday, May 17th
"""

def bubble_sort(alist):
    """ Sorts integers using bubble sort, takes n passes
    Author: Chris Specht
    Args:
        alist (list):
    """
    for sortedlist in range(len(alist) - 1, 0, -1): # always takes n passes
        for i in range(len(sortedlist)):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist


def bubble_sort2(alist):
    """
    Author: Chris Specht
    """
    pass


def insertion_sort(alist):
    """
    Author: Koichi Kodama
    """
    for x in range(len(alist)):
        insertion_helper(alist, x)


def insertion_helper(alist, start):
    x = alist[start]
    z = start
    while z > 0 and alist[z - 1] > x:
        alist[z] = alist[z - 1]
        z -= 1
    alist[z] = x
    return alist


def selection_sort(alist):
    """
    Authors:
        Chris Specht
        Koichi Kodama
    """

    pass


def quick_sort(alist):
    """
    Author: Koichi Kodama
    """
    pass


def merge_sort(alist):
    """
    Author: Chris Specht
    """
    pass


def heap_sort(alist):
    """
    Authors:
        Chris Specht
        Koichi Kodama
    """
    pass