class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            map[n] = map.get(n, 0) + 1

        for num, frq in map.items():
            freq[frq].append(num)

        print(freq)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
            if len(res) == k:
                return res
        return res