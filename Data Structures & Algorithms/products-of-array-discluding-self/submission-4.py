class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_cnt = 0

        for n in nums:
            if n:
                prod *= n
            else:
                zero_cnt += 1

        if zero_cnt > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, n in enumerate(nums):
            if zero_cnt:
                if n:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod//n
        return res