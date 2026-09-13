class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        result = []

        for s in strs:
            ss = "".join(sorted(s))
            groups.setdefault(ss, []).append(s)

        for k,v in groups.items():
            result.append(v)

        return result