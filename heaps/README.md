## Heaps 
Datastructures that organizes elements based on priority, Higher priority element is at the top of the heap.

Effecient access of higher priority item
- Min-heap: prioritizes the smallest element by keeping it a top of the heap
- Max-heap: prioritizes the largest element by keeping it a top of the heap

Underlying data structure: Complete Binary Tree
- The binary tree + satisfy the heap property: each node in the tree has a value that is less than or equal to the values of both its children.
- Array representation of heap: [1, 2, 4, 5, 8, 6, 9]: For a node at i, Left Child	2 * i + 1, Right: 2 * i + 2
- All levels of the tree are fully filled except for the last level


In min heap, node's value is less than or equal to that of the children
- Insert: O(log(n))
- Deletion: O(log(n))
- Peek: O(1)
- Heapify: O(n) # Transforms an unsorted list of values into a heap

Priority queue: with custom logic on how to prioritize based on the custom logic

Real world Applications:
- Managing tasks in OS

# How to identify:
"Top K" problems
