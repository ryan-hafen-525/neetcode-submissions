class Solution:

    def isPalindrome(self, s: str) -> bool:
        punc = "&!.,?':\" "
        result = "".join([c.lower() for c in s if c not in punc])

        return result == result[::-1]