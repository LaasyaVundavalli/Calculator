"""
Searching algorithms module.

This module contains implementations of various searching algorithms with step-by-step output.
"""

def binary_search(arr, target):
    """
    Binary Search algorithm.

    Assumes the array is sorted.
    Time Complexity: O(log n)
    """
    steps = []
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        steps.append(f"Left: {left}, Right: {right}, Mid: {mid} (value: {arr[mid]})")
        if arr[mid] == target:
            steps.append(f"Found {target} at index {mid}")
            return mid, steps, "O(log n)"
        elif arr[mid] < target:
            left = mid + 1
            steps.append(f"{target} > {arr[mid]}, search right half")
        else:
            right = mid - 1
            steps.append(f"{target} < {arr[mid]}, search left half")
    steps.append(f"{target} not found in array")
    return -1, steps, "O(log n)"


# Dictionary to map algorithm names to functions
SEARCHING_ALGORITHMS = {
    "Binary Search": binary_search,
}