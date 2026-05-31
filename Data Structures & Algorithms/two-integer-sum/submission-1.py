class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == x:
                    return [i, j]
                else:
                    continue
        return [-1, -1]
