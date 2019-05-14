""" Lab 6: Sorting Algorithms
Chris Specht
Koichi Kodama
CPE 202-09
Spring 2019
Due Friday, May 17th
"""


import random
import time


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


def bubble_sort2(alist): # TESTED, works
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


def insertion_sort(alist):
    """Sorts a list through Insertion sort
    Author: Koichi Kodama
    Args:
        alist (list): List to be sorted through
    Returns:
        alist (list): Sorted List
    """
    comparisons = 0
    for x in range(len(alist)):
        insert = alist[x]
        iterate = x
        while iterate > 0 and alist[iterate - 1] > x:
            alist[iterate] = alist[iterate - 1]
            iterate -= 1
            comparisons += 1
        alist[iterate] = insert
        comparison += 1
    return comparisons 


def selection_sort(alist):
    """ Sorts list of integers using selection sort
    Authors:
        Chris Specht
        Koichi Kodama
    Args:
        alist (list): list of unsorted integers
    Returns:
        int: number of comparisons
    """
    comparison = 0
    for i in range(len(alist)): 
    
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i + 1, len(alist)):
            comparison += 1 
            if alist[min_idx] > alist[j]: 
                min_idx = j 
                
        # Swap the found minimum element with  
        # the first element         
        alist[i], alist[min_idx] = alist[min_idx], alist[i]
    return comparison


def quick(arr, low, high, comparison): 
    i = (low - 1) 
    pivot = arr[high] 

    for j in range(low , high):
        if arr[j] <= pivot: 
            i = i + 1 
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return i + 1, comparison


def quickSort(arr, low, high, comparison = None):
    """
    Author: Koichi Kodama
    """
    if comparison == None:
        comparison = 0
    if low < high:
        pi = quick(arr, low, high, comparison)
        quickSort(arr, low, pi - 1, comparison) 
        quickSort(arr, pi + 1, high, comparison)
    return 


def merge_sort(alist, comparisons=None): # TESTED, works
    """ Sorts list of integers using merge sort
    Author: Chris Specht
    Args:
        alist (list): list of unsorted integers
        comparisons (NoneType/int): counts total number of comparisons
    Returns:
        list: [0] sorted list
        int: [1] number of comparisons 
    """
    # base case, one or zero elements in list
    if len(alist) <= 1:
        return (alist, 0)
    # calculate midpoint, recursively call with left and right halves
    midpoint = len(alist) // 2
    left = merge_sort(alist[:midpoint], comparisons)
    right = merge_sort(alist[midpoint:], comparisons)
    return merge(left[0], right[0], left[1] + right[1])


def merge(left, right, comparisons): # TESTED, works
    """ Merges two sorted lists
    Author: Chris Specht
    Args:
        left (list): lefthand list
        right (list): righthand list
    Returns:
        list: merged list
        int: number of comparisons
    """
    a_idx, b_idx = 0, 0
    merged = []
    if not comparisons:
        comparisons = 0
    # while both left and right are not empty
    while a_idx < len(left) and b_idx < len(right):
        # if value on left is <= value on right, add left value to list
        if left[a_idx] <= right[b_idx]:
            merged.append(left[a_idx])
            a_idx += 1
        # if value on left is > value on right, add right value to list
        else:
            merged.append(right[b_idx])
            b_idx += 1
        comparisons += 1
    # add rest of unused list right to merged
    if a_idx == len(left):
        merged.extend(right[b_idx:])
    # add rest of unused list left to merged
    else:
        merged.extend(left[a_idx:])
    # return merged, comparisons
    return merged, comparisons


def heap_sort(alist):
    """ Sorts list of integers using heap sort
    Authors:
        Chris Specht
        Koichi Kodama
    """
    pass


def main():

    # # Creates random list of 10 integers
    # random.seed(1) #in order to generate the same sequence of numbers each time.
    # alist = random.sample(range(10000),10)

    # # Times a sorting algorithm
    # start_time = time.time()
    # #Now call sort function (.sort())
    # end_time = time.time()
    # sort_time = end_time – start_time

    pass


if __name__ == "__main__":
    main()