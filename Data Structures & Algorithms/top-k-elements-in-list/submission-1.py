class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        temp = [[] for i in range(len(nums)+1)]
        result = []
        for n in nums:
            map[n] += 1
        
        for num, frq in map.items():
            temp[frq].append(num)
        
        for num in range(len(temp)-1, 0, -1):
            for n in temp[num]:
                result.append(n)
                if len(result) == k:
                    return result
