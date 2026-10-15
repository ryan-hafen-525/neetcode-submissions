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
            next_start = start + 1
            while next_start < len(candidates) and candidates[next_start] == candidates[start]:
                next_start += 1
            backtrack(next_start, current, total)

        backtrack(0, [], 0)

        return results