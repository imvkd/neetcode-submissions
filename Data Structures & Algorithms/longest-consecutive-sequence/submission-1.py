class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for num in num_set:
            if num-1 not in num_set:
                curr_res = 1
                while num+curr_res in num_set:
                    curr_res += 1
                res = max(res, curr_res)
        return res