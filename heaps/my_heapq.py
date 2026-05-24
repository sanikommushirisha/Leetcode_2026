import heapq

arr = [3, 1, 4, 1, 5, 9, 2]

### MIN HEAP
heapq.heapify(arr)

heapq.heappush(arr, 0) # push 0 to the heap. O(log n)

arr[0] # peek

min_element = heapq.heappop(arr) # pop and return the min element = 0. O(log n)

# peek the new min element = 1. O(1)
arr[0]


### MAX HEAP
negated_arr = [-x for x in arr]
heapq.heapify(negated_arr)

heapq.heappush(negated_arr, -11) # push 11 to the heap by negating it

negated_arr[0] # peek root of heap = -11

max_element = -heapq.heappop(negated_arr) # pop and return the max element = -11

negated_arr[0] # peek the new max element = 9


## STORING TUPLES: 
# By default, the heap is ordered based on the first element of the tuple. 
# If the first elements are equal, the second elements are compared, and so on.

arr = [(3, 1), (1, 5), (4, 2), (1, 9), (5, 3), (9, 4), (2, 6)]

heapq.heapify(arr)

min_element = heapq.heappop(arr) # pop and return the min element = (1, 5)

arr[0] # peek the new min element = (1, 9)

heapq.heappush(arr, (1, 7)) # push (1, 7) to the heap, which is smaller than (1, 9)

arr[0] # peek the min element = (1, 7)