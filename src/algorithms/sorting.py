"""
Sorting algorithms module.

This module contains implementations of various sorting algorithms with step-by-step output.
"""

import time


def bubble_sort(arr):
    """
    Bubble Sort algorithm.

    Time Complexity: O(n^2)
    """
    n = len(arr)
    steps = []
    arr_copy = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        steps.append(f"Pass {i+1}: {arr_copy.copy()}")
        if not swapped:
            break
    return arr_copy, steps, "O(n^2)"


def selection_sort(arr):
    """
    Selection Sort algorithm.

    Time Complexity: O(n^2)
    """
    n = len(arr)
    steps = []
    arr_copy = arr.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
        steps.append(f"Pass {i+1}: {arr_copy.copy()}")
    return arr_copy, steps, "O(n^2)"


def insertion_sort(arr):
    """
    Insertion Sort algorithm.

    Time Complexity: O(n^2)
    """
    n = len(arr)
    steps = []
    arr_copy = arr.copy()
    for i in range(1, n):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
        steps.append(f"After inserting {key}: {arr_copy.copy()}")
    return arr_copy, steps, "O(n^2)"


def quick_sort(arr):
    """
    Quick Sort algorithm.

    Time Complexity: O(n log n) average
    """
    steps = []

    def _quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            steps.append(f"Partition at {pi}: {arr.copy()}")
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    arr_copy = arr.copy()
    _quick_sort(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy, steps, "O(n log n) average"


def merge_sort(arr):
    """
    Merge Sort algorithm.

    Time Complexity: O(n log n)
    """
    steps = []

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        steps.append(f"Merging {left} and {right} -> {result}")
        return result

    def _merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = _merge_sort(arr[:mid])
        right = _merge_sort(arr[mid:])
        return merge(left, right)

    arr_copy = arr.copy()
    sorted_arr = _merge_sort(arr_copy)
    return sorted_arr, steps, "O(n log n)"


def heap_sort(arr):
    """
    Heap Sort algorithm.

    Time Complexity: O(n log n)
    """
    steps = []
    arr_copy = arr.copy()

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr_copy)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr_copy, n, i)
    for i in range(n - 1, 0, -1):
        arr_copy[i], arr_copy[0] = arr_copy[0], arr_copy[i]
        steps.append(f"Extract max: {arr_copy.copy()}")
        heapify(arr_copy, i, 0)
    return arr_copy, steps, "O(n log n)"


# Dictionary to map algorithm names to functions
SORTING_ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
}