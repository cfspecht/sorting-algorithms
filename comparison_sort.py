""" Lab 6: Sorting Algorithms
Chris Specht
Koichi Kodama
CPE 202-09
Spring 2019
Due Monday, May 20th
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
    for sorted_list in range(len(alist) - 1, 0, -1): # always takes n passes
        for i in range(sorted_list):
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
    for sorted_list in range(len(alist) - 1, 0, -1): # one pass through the list
        is_sorted = True # will remain true if no swaps are made
        for i in range(sorted_list):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                is_sorted = False
            comparisons += 1
        if is_sorted:
            return comparisons
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
        comparisons += 1

        key = alist[i]

        # Move elements of alist[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < alist[j]:
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


Counter = 0
def quick_sort(array, start=0, end=None, comparisons=None):
    """ Sorts integers using quick sort
    Authors:
        Chris Specht
        Koichi Kodama
    Args:
        array (list): unsorted integers
        start (int): starting index of current call
        end (int/NoneType): ending index of current call
        comparisons (int/NoneType): number of comparisons
    Returns:
        comparisons (int/NoneType): number of comparisons
    """
    global Counter
    # for very first call of function
    if end is None:
        end = len(array) - 1
    if not comparisons:
        comparisons = 0

    size = (end - start) + 1
    midpoint = (start + end) // 2

    # if size > 1, if list is longer than 1 element
    if size > 1:

        # set pivot to mid point value
        pivot = array[midpoint]

        # swap the start and midpoint values
        array[start], array[midpoint] = array[midpoint], array[start]

        # set left = start + 1, right = end
        left = start + 1
        right = end

        # while left <= right
        while left <= right:

            # increment left while left <= end and its value < pivot
            while left <= end and array[left] < pivot:
                left += 1
                Counter += 1

            # increment right while right > start and its value >= pivot
            while right > start and array[right] >= pivot:
                right -= 1
                Counter += 1

            # if left index < right index
            if left < right:
                # swap values
                array[left], array[right] = array[right], array[left]

        # swap pivot value and right value back
        # puts pivot value back in original place
        array[start], array[right] = array[right], array[start]

        # recursive call on each half
        quick_sort(array, start, right - 1, comparisons)
        quick_sort(array, right + 1, end, comparisons)

    return Counter


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
    for i in range(len(alist) - 1, 0, -1):

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
    """ Runs test with all list sizes for all functions
    """

    # full list sizes
    list_sizes = [1000, 2000, 4000, 8000, 16000, 32000, 100000, 500000]

    # BUBBLE SORT
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

    print()
    print("=" * 30)
    print()

    # BUBBLE SORT 2
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

    print()
    print("=" * 30)
    print()

    # INSERTION SORT
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
        print()

    print()
    print("=" * 30)
    print()

    # SELECTION SORT
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

    print()
    print("=" * 30)
    print()

    # QUICK SORT
    for list_size in list_sizes:
        random.seed(1)
        alist = random.sample(range(500001), list_size)
        start_time = time.time()
        comparisons = quick_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Quick sort (unsorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Quick sort (unsorted), size: %s, time: %s" % (list_size, sort_time))

        start_time = time.time()
        comparisons = quick_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Quick sort (sorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Quick sort (sorted), size: %s, time: %s" % (list_size, sort_time))
        print()

    print()
    print("=" * 30)
    print()

    # MERGE SORT
    for list_size in list_sizes:
        random.seed(1)
        alist = random.sample(range(500001), list_size)
        start_time = time.time()
        comparisons = merge_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Merge sort (unsorted), size: %s, comparisons: %s" % (list_size, comparisons[1]))
        print("Merge sort (unsorted), size: %s, time: %s" % (list_size, sort_time))

        start_time = time.time()
        comparisons = merge_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Merge sort (sorted), size: %s, comparisons: %s" % (list_size, comparisons[1]))
        print("Merge sort (sorted), size: %s, time: %s" % (list_size, sort_time))
        print()

    print()
    print("=" * 30)
    print()

    # HEAP SORT
    for list_size in list_sizes:
        random.seed(1)
        alist = random.sample(range(500001), list_size)
        start_time = time.time()
        comparisons = heap_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Heap sort (unsorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Heap sort (unsorted), size: %s, time: %s" % (list_size, sort_time))

        start_time = time.time()
        comparisons = heap_sort(alist)
        end_time = time.time()
        sort_time = end_time - start_time
        print("Heap sort (sorted), size: %s, comparisons: %s" % (list_size, comparisons))
        print("Heap sort (sorted), size: %s, time: %s" % (list_size, sort_time))
        print()

    # TIM SORT
    for list_size in list_sizes:
        random.seed(1)
        alist = random.sample(range(500001), list_size)
        start_time = time.time()
        alist.sort()
        end_time = time.time()
        sort_time = end_time - start_time
        print("Tim sort (unsorted), size: %s, time: %s" % (list_size, sort_time))

        start_time = time.time()
        alist.sort()
        end_time = time.time()
        sort_time = end_time - start_time
        print("Tim sort (sorted), size: %s, time: %s" % (list_size, sort_time))
        print()


if __name__ == "__main__":
    main()
