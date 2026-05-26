def letterCombinations(digits):
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    all = []


    def backtrack(candidate, index):
        if index == len(digits):
            all.append("".join(candidate))
            return
        
        curr_digit = digits[index]
        curr_str = phone[curr_digit]

        for curr_char in curr_str:
            candidate.append(curr_char)
            backtrack(candidate, index + 1);
            candidate.pop()

    backtrack([], 0)
    return all

print(letterCombinations("23"))