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
    """Sorts a list through Insertion sort
    
    Args:
        alist (list): List to be sorted through
    Returns:
        alist (list): Sorted List
    """
    for x in range(len(alist)):
        insert = alist[x]
        iterate = x
        while iterate > 0 and alist[iterate - 1] > x:
            alist[iterate] = alist[iterate - 1]
            iterate -= 1
        alist[iterate] = insert
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