""" Lab 6: Sorting Algorithms
Chris Specht
Koichi Kodama
CPE 202-09
Spring 2019
Due Friday, May 17th
"""

def bubble_sort(alist): # TESTED, works
    """ Sorts integers using bubble sort, takes n passes
    Author: Chris Specht
    Args:
        alist (list): unsorted list of integers
    Returns:
        int: number of comparisons
    """
    comparisons = 0
    for sortedList in range(len(alist) - 1, 0, -1): # always takes n passes
        for i in range(sortedList):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                comparisons += 1
    return comparisons


ints = [3, 2, 1, 4, 5]
print("Number of comparisons: " + str(bubble_sort(ints)))
print(ints)


def bubble_sort2(alist):
    """ Sorts integers using bubble sort, stops immediately once sorted
    Author: Chris Specht
    Args:
        alist (list): unsorted list of integers
    Returns:
        int: number of comparisons
    """
    comparisons = 0
    isSorted = False
    while not isSorted:
        for sortedList in range(len(alist) - 1, 0, -1): # always takes n passes
            isSorted = True # will remain true if no swaps are made
            for i in range(sortedList):
                if alist[i] > alist[i + 1]:
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
                    isSorted = False
                    comparisons += 1
    return comparisons


ints = [3, 2, 1, 4, 5]
print("Number of comparisons: " + str(bubble_sort2(ints)))
print(ints)



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