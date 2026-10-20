class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(i, current: list):
            if len(current) == len(nums):
                results.append(current[:])
                return 
            
            for j in range(len(nums)):
                if nums[j] in current:
                    continue

                current.append(nums[j])
                dfs(i + 1, current)
                current.pop()
            
        dfs(0, [])

        return results