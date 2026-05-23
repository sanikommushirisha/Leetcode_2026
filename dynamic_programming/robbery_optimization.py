

class OptimizedRobbery:
    def optimize(houses):
        if len(houses) == 0:
            return 0
        
        dp = [0] * len(houses)
        dp[0] = houses[1]
        dp[1] = max(houses[0], houses[1])

        for i in range(2, len(houses)):
            dp[i] = max(dp[i - 1], houses[i] + dp[i - 2])

        return dp[len(houses) - 1]



if __name__ == "__main__":
    houses = [200, 300, 200, 50]
    print(OptimizedRobbery.optimize(houses))