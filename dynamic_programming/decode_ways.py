
class DecodeWays:
    def __init__(self):
        self.memo = {}

    def is_valid(self, c: str):
        if c.startswith("0"):
            return False
        try:
            int_c = int(c)
            return int_c > 0 and int_c <= 26
        except Exception:
            return False
        

    def num_decodings(self, s: str, i: int) -> int:
        if i > len(s):
            return 0
        if i == len(s):
            return 1
        
        way1 = self.num_decodings(s, i + 1) if self.is_valid(s[i]) else 0
        way2 = self.num_decodings(s, i + 2) if self.is_valid(s[i:i+2]) else 0

        return way1 + way2
    
    
    
    def num_decodings_dp(self, s):
        if len(s) == 0:
            return 0
        
        n = len(s)
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if self.is_valid(s[0]) else 0
        for i in range(2, n + 1):
            if self.is_valid(s[i - 1]):
                dp[i] += dp[i - 1]
            if i>=2 and self.is_valid(s[i-2:i]):
                dp[i] += dp[i - 2]
        return dp[n]


#227 -> 2 -> '27', 
#    -> 2 -> 2 -> 7
#         -> 27  invalid     
#    -> 22 -> 7
if __name__ == "__main__":
    test_cases = [
        ("12", 2),        # "AB" (1,2), "L" (12)
        ("226", 3),       # "BZ" (2,26), "VF" (22,6), "BBF" (2,2,6)
        ("06", 0),        # leading zero -> invalid
        ("10", 1),        # "J" (10) only
        ("27", 1),        # "BG" (2,7) only -- 27 not valid
        ("11106", 2),     # "AAJF" (1,1,10,6), "KJF" (11,10,6)
    ]

    decoder = DecodeWays()
    for s, expected in test_cases:
        result = decoder.num_decodings_dp(s)
        print(f"s={s!r:10} expected={expected} got={result} {'OK' if result == expected else 'FAIL'}")
