

class ClimbStairs:
    def __init__(self):
        self.memo = {}

    def climb_stairs(self, n) -> int:
        if n <= 2:
            return n

        if n in self.memo:
            return self.memo[n]


        self.memo[n] = self.climb_stairs(n-1) + self.climb_stairs(n-2)
        return self.memo[n]
    
    def climb_stairs_bottom_up(self, n) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
    # We only ever need to access the previous two values of the DP array
    def climb_stairs_optimized(self, n) -> int:
        if n <= 2:
            return n
         
        before, after = 1, 2
        for i in range(3, n + 1):
            next = before + after
            before = after
            after = next
        
        return after

if __name__ == "__main__":
    print(ClimbStairs().climb_stairs_optimized(7))