class Solution:

    def isPalindrome(self, s: str) -> bool:
        punc = "&!.,?':\" "
        result = [c.lower() for c in s if c not in punc]

        return "".join(result) == "".join(result)[::-1]