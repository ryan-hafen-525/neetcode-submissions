class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "~emptyArray~"

        return "~~".join(strs)

    def decode(self, s: str) -> List[str]:
        val = s.split("~~")
        
        if val == ["~emptyArray~"]:
            return []
        
        return val