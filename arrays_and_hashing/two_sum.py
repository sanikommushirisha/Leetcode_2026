"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Tags: [array, hash-map]

Approach:
    Use a hash map to store each number's index as we iterate.
    For each number, check if (target - num) already exists in the map.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i
        
        return []


# --- Tests ---
def test():
    s = Solution()
    assert s.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert s.two_sum([3, 2, 4], 6) == [1, 2]
    assert s.two_sum([3, 3], 6) == [0, 1]
    print("All tests passed!")


if __name__ == "__main__":
    test()
