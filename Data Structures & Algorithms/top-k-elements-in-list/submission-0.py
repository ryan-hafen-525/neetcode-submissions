class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)

        s_freqs = dict(sorted(freqs.items(), key = lambda item: item[1]))

        result = []

        for i in range(k):
            result.append(list(s_freqs)[i-k])

        return result