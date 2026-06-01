class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return 1

        l, r = 0, 1
        res = 1
        ss = s[l]

        while r < len(s):
            if s[r] not in ss:
                ss += s[r]
                res = max(res, len(ss))
                r += 1
            else:
                l += 1
                ss = s[l]
                r = l+1
        print(ss)
        return res