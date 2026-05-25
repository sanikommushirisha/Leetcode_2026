class Solution:
    def combinationSum(self, candidates, target):
        all = []
        def cSum(start, candidate, currTarget):
            if currTarget == 0:
                all.append(candidate[:])
                return
            
            if currTarget < 0:
                return
            
            for i in range(start, len(candidates)):
                candidate.append(candidates[i])
                cSum(i, candidate, currTarget - candidates[i])
                candidate.pop()

        cSum(0, [], target)
        return all


print(Solution().combinationSum([2,3,6,7], 7))