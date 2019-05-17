""" Lab 6: Sorting Algorithms
Chris Specht
Koichi Kodama
CPE 202-09
Spring 2019
Due Friday, May 17th
"""


import random
import time

# IMPORTANT NOTE

    # nohup ... &
    # ^ for running on server


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
    # Traverse through 1 to len(alist) 
    for i in range(1, len(alist)): 
  
        key = alist[i] 
  
        # Move elements of alist[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < alist[j] : 
                alist[j + 1] = alist[j] 
                j -= 1
                comparisons += 1
        alist[j + 1] = key
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
        min_idx = i 
        for j in range(i + 1, len(alist)):
            if alist[min_idx] > alist[j]: 
                min_idx = j 
            comparison += 1     
        alist[i], alist[min_idx] = alist[min_idx], alist[i]
    return comparison


def partition(arr,low,high, comparisons): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high):
        comparisons += 1
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 , comparisons) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr, low, high, comparisons = None):
    if comparisons == None:
        comparisons = 0
    if low < high:
    
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high, comparisons)

        # Separately sort elements before
        # partition and after partition
        lower = quickSort(arr, low, pi[0]-1, pi[1])
        higher = quickSort(arr, pi[0]+1, high, pi[1])
        comparisons = comparisons + higher + lower
    return comparisons


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
    Args:
        alist (list): list of integers to be sorted
    Returns:
        int: number of comparisons
    """
    # build max heap from list, alist is now a heap
    comparisons = max_heapify(alist)

    # growing the sorted sublist at end
    for i in range (len(alist) - 1, 0, -1):

        # switch first and last value
        alist[i], alist[0] = alist[0], alist[i]
        # properly order modified heap
        comparisons += shift_down(alist, 0, i)

    return comparisons


def max_heapify(alist):
    """ Heapifies an unsorted list
    Args:
        alist (list): list to be heapified
    Returns:
        int: number of comparisons
    """
    # initialize comparisons
    comparisons = 0

    # get parent of last item, shift down
    size = len(alist)

    # call shift_down on every index, starting from the end
    for i in range(size, -1, -1):
        comparisons += shift_down(alist, i, size)

    return comparisons


def shift_down(heap, i, size, comparisons=None):
    """ Shifts newly added item at top of heap to its proper place
    Args:
        heap (list): heap to be modified
        i (int): root index of current call of function
        size (int): size of the heap (actual size, not index)
    Returns:
        int: number of comparisons
    """
    if not comparisons:
        comparisons = 0

    # calculate indices of root, left, and right children of current root
    root_index = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    # get index of minimum child, choosing the larger child
    if left_index < size and heap[left_index] > heap[root_index]:
        root_index = left_index # shifts pointer down
    if right_index < size and heap[right_index] > heap[root_index]:
        root_index = right_index # shifts pointer down

    comparisons += 2

    # if root index has changed, swap values
    if root_index != i:
        heap[root_index], heap[i] = heap[i], heap[root_index]
        comparisons += 1
        # recursive call on subheap
        comparisons += shift_down(heap, root_index, size, comparisons)

    # base case is if current node has no children or node is in correct place
    return comparisons


def main():

    # # Creates random list of 10 integers
    # random.seed(1) #in order to generate the same sequence of numbers each time.
    # alist = random.sample(range(10000),10)

    # # Times a sorting algorithm
    # start_time = time.time()
    # #Now call sort function (.sort())
    # end_time = time.time()
    # sort_time = end_time – start_time

    # alist = random.sample(range(500001), 16000) # second argument is number of items in random list created
    # start_time = time.time()
    # comparisons = bubble_sort(alist) # this is where the sorting algorithm goes

    # # bubble_sort
    # random.seed(1)
    # alist = random.sample(range(500001), 1000)
    # start_time = time.time()
    # comparisons = insertion_sort(alist)
    # end_time = time.time()
    # sort_time = end_time - start_time
    # print("Bubble sort comparisons: " + str(comparisons))
    # print("Bubble sort time: " + str(sort_time))



# =================================================================================================

    # it will always generate same list, so it doesn't all have to run at once

    # # full list sizes
    # list_sizes = [1000, 2000, 4000, 8000, 16000, 32000, 100000, 500000]

    # # hard, time-consuming ones
    # list_sizes = [32000, 100000, 500000]

    # easy, short ones
    list_sizes = [1000, 2000, 4000, 8000, 16000]

    # BUBBLE SORT
    # iterate through each list size
    for list_size in list_sizes:
        random.seed(1)
        alist = random.sample(range(500001), list_size)
        start_time = time.time()
        comparisons = bubble_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Bubble sort (unsorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Bubble sort (unsorted), size: %s, time: %s" % (list_size, sort_time))
        
        start_time = time.time()
        comparisons = bubble_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Bubble sort (sorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Bubble sort (sorted), size: %s, time: %s" % (list_size, sort_time))
        print()


    print("=" * 30)
    print()

    # BUBBLE SORT 2
    # iterate through each list size
    for list_size in list_sizes:
        random.seed(1)
        alist = random.sample(range(500001), list_size)
        start_time = time.time()
        comparisons = bubble_sort2(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Bubble sort 2 (unsorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Bubble sort 2 (unsorted), size: %s, time: %s" % (list_size, sort_time))
        
        start_time = time.time()
        comparisons = bubble_sort2(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Bubble sort 2 (sorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Bubble sort 2 (sorted), size: %s, time: %s" % (list_size, sort_time))
        print()

    print("=" * 30)
    print()

    
    # INSERTION SORT
    # iterate through each list size
    for list_size in list_sizes:
        random.seed(1)
        alist = random.sample(range(500001), list_size)
        start_time = time.time()
        comparisons = insertion_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Insertion sort (unsorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Insertion sort (unsorted), size: %s, time: %s" % (list_size, sort_time))
        
        start_time = time.time()
        comparisons = insertion_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Insertion sort (sorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Insertion sort (sorted), size: %s, time: %s" % (list_size, sort_time))
    

    print("=" * 30)
    print()
    
    # SELECTION SORT
    # iterate through each list size
    for list_size in list_sizes:
        random.seed(1)
        alist = random.sample(range(500001), list_size)
        start_time = time.time()
        comparisons = selection_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Selection sort (unsorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Selection sort (unsorted), size: %s, time: %s" % (list_size, sort_time))
        
        start_time = time.time()
        comparisons = selection_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Selection sort (sorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Selection sort (sorted), size: %s, time: %s" % (list_size, sort_time))
        print()

    print("=" * 30)
    print()

    # TODO recursion error reached
    # QUICK SORT
    # iterate through each list size
    for list_size in list_sizes:
        random.seed(1)
        alist = random.sample(range(500001), list_size)
        start_time = time.time()
        comparisons = quickSort(alist, 0, len(alist) - 1)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Quick sort (unsorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Quick sort (unsorted), size: %s, time: %s" % (list_size, sort_time))
        start_time = time.time()
        comparisons = quickSort(alist, 0, len(alist) - 1)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Quick sort (sorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Quick sort (sorted), size: %s, time: %s" % (list_size, sort_time))
        print()

    print("=" * 30)
    print()

    # MERGE SORT
    # iterate through each list size
    for list_size in list_sizes:
        random.seed(1)
        alist = random.sample(range(500001), list_size)
        start_time = time.time()
        comparisons = merge_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Merge sort (unsorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Merge sort (unsorted), size: %s, time: %s" % (list_size, sort_time))
        
        start_time = time.time()
        comparisons = merge_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Merge sort (sorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Merge sort (sorted), size: %s, time: %s" % (list_size, sort_time))
        print()


    # ints = [1, 4, 3, 2]
    # shift_down(ints, 0, 4)
    # print(ints)

    # ints = [5, 3, 7, 8, 11]
    # comparisons = max_heapify(ints)
    # print(ints)
    # print(comparisons)

    # ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # max_heapify(ints)
    # print(ints)

    # ints = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # comparisons = heap_sort(ints)
    # print(ints)
    # print(comparisons)


if __name__ == "__main__":
    main() 
