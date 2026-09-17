class Solution:

    def isPalindrome(self, s: str) -> bool:
        punc = "&!.,?':\""
        joined = s.replace(" ", "")
        result = []

        for c in joined:
            if c not in punc:
                result.append(c.lower())

        return "".join(result) == "".join(result)[::-1]