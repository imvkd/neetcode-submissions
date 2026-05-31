class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def findCombinations(indx, nums, target, res, ds):
            if indx == len(nums):
                if target == 0:
                    res.append(ds.copy())
                return
        
            if nums[indx] <= target:
                ds.append(nums[indx])
                findCombinations(indx, nums, target-nums[indx], res, ds)
                ds.pop()

            findCombinations(indx+1, nums, target, res, ds)

        res = []
        findCombinations(0, nums, target, res, [])
        return res


