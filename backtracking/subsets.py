from typing import List, Set

all = []
def find_all_subsets(nums: List[int]) -> List[List[int]]:
    backtrack(nums, [], 0)
    return all

def backtrack(nums: List[int], candidate: List[int], i) -> None:
    if i > len(nums):
        return 
    
    all.append(candidate[:])
    
    for j in range(i, len(nums)):
        candidate.append(nums[j])
        backtrack(nums, candidate, j + 1)
        candidate.pop()

print(find_all_subsets([1, 2, 3]))
