class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dupes: dict = {}

        for letter in s:
            if letter in dupes:
                dupes[letter] += 1
            else:
                dupes[letter] = 1

        for letter in t:
            if letter in dupes:
                if dupes[letter] >= 1:
                    dupes[letter] -= 1
                else: 
                    return False
            else:
                return False

        return True