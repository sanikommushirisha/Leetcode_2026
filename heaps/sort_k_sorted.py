from typing import List
import heapq


# Given an integer array where each element is at most k positions away from its sorted position, 
# sort the array in a non-decreasing order.

# Example:
# Input: nums = [5, 1, 9, 4, 7, 10], k = 2
# Output: [1, 4, 5, 7, 9, 10]

def sort_a_k_sorted_array(nums: List[int], k: int) -> List[int]:
    # Populate a min-heap with the first k + 1 values in 'nums'.
    min_heap = nums[:k+1]
    heapq.heapify(min_heap)
    # Replace elements in the array with the minimum from the heap at each
    # iteration.
    insert_index = 0
    for i in range(k + 1, len(nums)):
        nums[insert_index] = heapq.heappop(min_heap)
        insert_index += 1
        heapq.heappush(min_heap, nums[i])
    # Pop the remaining elements from the heap to finish sorting the array.
    while min_heap:
        nums[insert_index] = heapq.heappop(min_heap)
        insert_index += 1
    return nums