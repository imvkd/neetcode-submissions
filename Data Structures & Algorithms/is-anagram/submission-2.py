class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ht1 = {}
        for char in s:
            ht1[char] = ht1.get(char, 0) + 1
        for char in t:
            if char not in ht1:
                return False
            ht1[char] -= 1
            if ht1[char] < 0:
                return False
        return True