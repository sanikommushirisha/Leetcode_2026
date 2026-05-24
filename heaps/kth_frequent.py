
# K largest elements: Why a min-heap of size K.
# heap[0] is the smallest element. If element > heap[0] add to min-heap

import heapq
from collections import Counter

def kth_frequent(strs, k):
    memo = {}
    kstrs = []
    for i in range(len(strs)):
        if strs[i] in memo:
            memo[strs[i]] += 1
        else:
            memo[strs[i]] = 1

    for elem, count in memo.items():
        if len(kstrs) < k:
            kstrs.append((count, elem))
            continue
        if len(kstrs) == k:
            heapq.heapify(kstrs)
        
        if count > kstrs[0][0]:
            heapq.heappop(kstrs)
            heapq.heappush(kstrs, (count, elem))

    return [elem for (count, elem) in kstrs]

class Pair:
   def __init__(self, str, freq):
       self.str = str
       self.freq = freq

   # Define a custom comparator.
   def __lt__(self, other):
       # Prioritize lexicographical order for strings with equal frequencies.
       if self.freq == other.freq:
           return self.str < other.str
       # Otherwise, prioritize strings with higher frequencies.
       return self.freq > other.freq


def kth_frequent_desc_order(strs, k):
    memo = {}
    for i in range(len(strs)):
        if strs[i] in memo:
            memo[strs[i]] += 1
        else:
            memo[strs[i]] = 1
    
    all_strs = [Pair(s, freq) for s, freq in memo.items()]
    heapq.heapify(all_strs)
    return [heapq.heappop(all_strs).str for i in range(0, k)]



 
#strs = ['go', 'coding', 'byte', 'byte', 'go', 'interview', 'go'], k = 2
# Output: ['go', 'byte']
print(kth_frequent_desc_order(['go', 'coding', 'byte', 'byte', 'go', 'interview', 'go'], 2))