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


def find_all_subsets_better_tc(nums):
    res = []
    backtrack1(0, [], nums, res)
    return res

def backtrack1(i, curr_subset, nums, res):
    # Base case: if all elements have been considered, add the current subset to the output.
    if i == len(nums):
        res.append(curr_subset[:])
        return
    # Include the current element and recursively explore all paths that branch from
    # this subset.
    curr_subset.append(nums[i])
    backtrack1(i + 1, curr_subset, nums, res)
    # Exclude the current element and recursively explore all paths that branch from
    # this subset.
    curr_subset.pop()
    backtrack1(i + 1, curr_subset, nums, res)


print(find_all_subsets_better_tc([1, 2, 3]))