class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1
            if map[n] > 1:
                return True
        return False