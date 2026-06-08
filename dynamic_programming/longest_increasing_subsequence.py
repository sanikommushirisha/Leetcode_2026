class LIS:
    def compute_lis(self, nums):
        if not nums:
            return 0
        
        dp = [1] * len(nums) # Since a single element is an increasing subsequence of length 1, we initialize dp with 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[len(nums) - 1]



if __name__ == "__main__":
    nums = [8,2,4,3,6,12]
    lis_count = LIS().compute_lis(nums)
    print(lis_count)

# 2, 5, 3, 4, 12
# 2, 5

# 2, 5, 3, 
# 2, 5


