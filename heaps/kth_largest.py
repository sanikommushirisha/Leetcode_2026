
# K largest elements: Why a min-heap of size K.
# heap[0] is the smallest element. If element > heap[0] add to min-heap

import heapq

def three_largest(nums):
    arr = nums[0:3]
    heapq.heapify(arr)

    for i in range(3, len(nums)):
        if nums[i] <= arr[0]:
            continue
        heapq.heappop(arr)
        heapq.heappush(arr, nums[i])

    return arr


print(three_largest([9, 3, 7, 1, -2, 6, 8]))