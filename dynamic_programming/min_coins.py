
class MinCoins:
    def __init__(self):
        self.memo = {}

    def min_coins(self, coins, target):
        if target == 0:
            return 0
        
        if target in self.memo:
            return self.memo[target]
        min_c = float('inf')
        
        for coin in coins:
            if coin <= target:
                min_c = min(min_c, 1 + self.min_coins(coins, target - coin))
        
        self.memo[target] = min_c
        return min_c
    
    def min_coins_bottom_up(self, coins, target):
        if target == 0:
            return 0
        
        dp = [float('inf')] * (target + 1)
        dp[0] = 0
        for i in range(1, target + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return dp[target] if dp[target] != float('inf') else -1
        

if __name__ == "__main__":
    coins, target = [1, 2, 3], 5
    print(MinCoins().min_coins_bottom_up(coins, target))


# Target 5
# use 1 => Target 4 => use 1 -> Target 3 -> 1 -> 2

#                   => use 2 -> Target 2 -
#                   => use 3 -> Target 1

# use 2 => Target 3
# use 3 => Target 2

# dp[i] = coin[i] + dp[]