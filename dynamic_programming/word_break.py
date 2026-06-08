class WordBreak:
    def word_break(self, s, word_dict):
        if len(s) == 0:
            return False

        dp = [False]*(len(s))
        dp[0] = True if s[0] in word_dict else False

        for i in range(1, len(s)):
            if s[0:i+1] in word_dict:
                dp[i] = True
                continue
            for j in range(0, i):
                if dp[j] and s[j+1:i+1] in word_dict:
                    print(i, j, s[j+1:i+1])
                    dp[i] = True
        print(dp)
        return dp[len(s) - 1]

if __name__ == "__main__":
    s = "leetcode"
    word_dict = ["leet","code"]
    sol = WordBreak().word_break(s, word_dict)
    print(sol)

# catsand
# cat -> True 
# cats -> True -> word[j:i] in dict + dp[i] true or word[0:i] in dict

