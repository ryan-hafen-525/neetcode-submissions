class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            ss = "".join(sorted(s))
            groups.setdefault(ss, []).append(s)

        return list(groups.values())