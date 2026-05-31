class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in map:
                return [map[diff]+1, i+1]
            map[numbers[i]] = i