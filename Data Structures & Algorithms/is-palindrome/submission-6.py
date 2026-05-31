import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        nospaces = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        print(nospaces)

        if len(nospaces) == 1:
            return True

        p1 = 0
        p2 = len(nospaces) - 1
        while p1 < p2:
            if nospaces[p1] != nospaces[p2]:
                return False
            p1+=1
            p2-=1
        return True