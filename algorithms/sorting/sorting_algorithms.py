"""
Sorting Algorithms Implementation in Python

This module contains implementations of various sorting algorithms
with detailed analysis and comparison.
"""

import time
import random
from typing import List, Callable


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort - Repeatedly steps through the list, compares adjacent elements
    and swaps them if they are in the wrong order.
    
    Time Complexity: O(n²) - Best: O(n), Average: O(n²), Worst: O(n²)
    Space Complexity: O(1)
    Stable: Yes
    In-place: Yes
    """
    arr = arr.copy()  # Don't modify original array
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr


def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort - Finds the minimum element and places it at the beginning.
    
    Time Complexity: O(n²) - Best: O(n²), Average: O(n²), Worst: O(n²)
    Space Complexity: O(1)
    Stable: No
    In-place: Yes
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort - Builds the sorted array one element at a time.
    
    Time Complexity: O(n²) - Best: O(n), Average: O(n²), Worst: O(n²)
    Space Complexity: O(1)
    Stable: Yes
    In-place: Yes
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort - Divide and conquer algorithm that divides the array into halves,
    sorts them, and then merges them.
    
    Time Complexity: O(n log n) - Best: O(n log n), Average: O(n log n), Worst: O(n log n)
    Space Complexity: O(n)
    Stable: Yes
    In-place: No
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Helper function for merge sort to merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort - Picks a pivot element and partitions the array around it.
    
    Time Complexity: O(n log n) - Best: O(n log n), Average: O(n log n), Worst: O(n²)
    Space Complexity: O(log n) - due to recursion stack
    Stable: No
    In-place: Yes (this implementation creates new arrays for clarity)
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort - Uses a binary heap data structure to sort.
    
    Time Complexity: O(n log n) - Best: O(n log n), Average: O(n log n), Worst: O(n log n)
    Space Complexity: O(1)
    Stable: No
    In-place: Yes
    """
    arr = arr.copy()
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr


def heapify(arr: List[int], n: int, i: int):
    """Helper function for heap sort to maintain heap property."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort - Non-comparison based sorting for integers in a small range.
    
    Time Complexity: O(n + k) where k is the range of input
    Space Complexity: O(k)
    Stable: Yes
    In-place: No
    """
    if not arr:
        return arr
    
    # Find the range of values
    min_val, max_val = min(arr), max(arr)
    range_val = max_val - min_val + 1
    
    # Create counting array
    count = [0] * range_val
    
    # Count occurrences
    for num in arr:
        count[num - min_val] += 1
    
    # Build result array
    result = []
    for i, freq in enumerate(count):
        result.extend([i + min_val] * freq)
    
    return result


# Utility functions for testing and analysis
def is_sorted(arr: List[int]) -> bool:
    """Check if array is sorted in ascending order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def generate_test_data(size: int, data_type: str = "random") -> List[int]:
    """Generate test data of different types."""
    if data_type == "random":
        return [random.randint(1, 1000) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(1, size + 1))
    elif data_type == "reverse":
        return list(range(size, 0, -1))
    elif data_type == "nearly_sorted":
        arr = list(range(1, size + 1))
        # Swap a few random pairs
        for _ in range(size // 10):
            i, j = random.randint(0, size - 1), random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    elif data_type == "duplicate":
        return [random.randint(1, 10) for _ in range(size)]
    else:
        raise ValueError(f"Unknown data type: {data_type}")


def benchmark_algorithm(algorithm: Callable, arr: List[int], name: str) -> float:
    """Benchmark a sorting algorithm and return execution time."""
    start_time = time.time()
    result = algorithm(arr)
    end_time = time.time()
    
    # Verify the result is sorted
    if not is_sorted(result):
        raise ValueError(f"{name} failed to sort the array correctly")
    
    return end_time - start_time


def compare_algorithms(size: int = 1000, data_type: str = "random"):
    """Compare all sorting algorithms on the same dataset."""
    algorithms = [
        (bubble_sort, "Bubble Sort"),
        (selection_sort, "Selection Sort"),
        (insertion_sort, "Insertion Sort"),
        (merge_sort, "Merge Sort"),
        (quick_sort, "Quick Sort"),
        (heap_sort, "Heap Sort"),
        (counting_sort, "Counting Sort")
    ]
    
    test_data = generate_test_data(size, data_type)
    print(f"\n=== Sorting {size} elements ({data_type} data) ===")
    print(f"{'Algorithm':<15} {'Time (ms)':<12} {'Status'}")
    print("-" * 35)
    
    results = []
    for algorithm, name in algorithms:
        try:
            if name == "Bubble Sort" and size > 10000:
                print(f"{'Bubble Sort':<15} {'Skipped':<12} Too slow for large data")
                continue
            
            time_taken = benchmark_algorithm(algorithm, test_data, name)
            results.append((name, time_taken))
            print(f"{name:<15} {time_taken*1000:<11.2f} ✓")
        except Exception as e:
            print(f"{name:<15} {'Error':<12} {str(e)}")
    
    return results


# Example usage and demonstration
if __name__ == "__main__":
    print("=== Sorting Algorithms Demo ===")
    
    # Test with small array for demonstration
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")
    
    algorithms = [
        (bubble_sort, "Bubble Sort"),
        (selection_sort, "Selection Sort"),
        (insertion_sort, "Insertion Sort"),
        (merge_sort, "Merge Sort"),
        (quick_sort, "Quick Sort"),
        (heap_sort, "Heap Sort"),
        (counting_sort, "Counting Sort")
    ]
    
    print("\nSorted results:")
    for algorithm, name in algorithms:
        sorted_array = algorithm(test_array)
        print(f"{name:<15}: {sorted_array}")
    
    # Performance comparison
    data_types = ["random", "sorted", "reverse", "nearly_sorted", "duplicate"]
    
    for data_type in data_types:
        compare_algorithms(1000, data_type)
    
    print("\n=== Performance on larger datasets ===")
    compare_algorithms(10000, "random")