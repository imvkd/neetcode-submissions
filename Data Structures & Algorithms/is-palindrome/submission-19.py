class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s2 = s.replace(" ", "").lower()
        # print(s2)
        s2 = s.lower()

        p1, p2 = 0, len(s2)-1

        while p1<p2:
            while not s2[p1].isalnum() and p1<p2:
                p1+=1
            while not s2[p2].isalnum() and p2>p1:
                p2-=1
            if s2[p1] != s2[p2]:
                return False
            p1+=1
            p2-=1
        return True