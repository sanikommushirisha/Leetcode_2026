from typing import List, Set

def find_all_permutations(nums: List[int]) -> List[List[int]]:
    all = []
    backtrack(nums, [], set(), all)
    return all

def backtrack(nums: List[int], candidate: List[int], used: Set[int], res: List[List[int]]) -> None:
    if len(candidate) == len(nums):
        print(candidate)
        res.append(candidate[:])
        return
    
    for num in nums:
        print(f"outside num {num} candidate {candidate} used {used}")
        if num not in used:
            # Add 'num' to the current permutation and mark it as used.
            candidate.append(num)
            used.add(num)
            print(f"num {num} candidate {candidate} used {used}")
            # Recursively explore all branches using the updated permutation candidate.
            backtrack(nums, candidate, used, res)
            used.remove(num)
            candidate.pop()
    print("-------")
    

print(find_all_permutations([1, 2, 3]))
