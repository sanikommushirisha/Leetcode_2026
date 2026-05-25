from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
  if not lists:
    return None
  
  non_empty = [head for head in lists if head]
  if not non_empty:
    return None
  
  heap = []
  for head in non_empty:
    heappush(heap, (head.val, id(head), head))
  
  dummy = ListNode(0)
  current = dummy
  
  while heap:
    val, _, node = heappop(heap)
    current.next = node
    current = current.next
    
    if node.next:
      heappush(heap, (node.next.val, id(node.next), node.next))
  
  return dummy.next
