class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed = {} # num: index

        for i in range(len(nums)):
            if target - nums[i] in passed:
                return [passed[target - nums[i]], i]
            
            passed[nums[i]] = i