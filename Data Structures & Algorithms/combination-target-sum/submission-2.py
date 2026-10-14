class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        sorted(nums)
        
        def backtrack(current, remaining):
            if not remaining:
                return

            for i in range(len(remaining) - 1, -1, -1):
                if sum(current) + remaining[i] < target:
                    current.append(remaining[i])
                    backtrack(current, remaining[:i+1])
                    current.pop()
                elif sum(current) + remaining[i] == target:
                    current.append(remaining[i])
                    results.append(current[:])
                    current.pop()                    

        backtrack([], nums)

        return results