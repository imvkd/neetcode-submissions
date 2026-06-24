class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
    
        for n in nums:
            map[n] = map.get(n, 0) + 1

        freq = [[] for i in range(len(nums)+1)]
        for key, val in map.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res