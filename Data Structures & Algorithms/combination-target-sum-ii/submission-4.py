class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(start, current, total):
            if total == target:
                results.append(current[:])
                return
            if start > len(candidates) - 1 or total > target:
                return

            current.append(candidates[start])
            backtrack(start + 1, current, total + candidates[start])
            current.pop()

            while start + 1 < len(candidates) and candidates[start] == candidates[start+1]:
                start += 1 
            backtrack(start + 1, current, total)

        backtrack(0, [], 0)

        return results