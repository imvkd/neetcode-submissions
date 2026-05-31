class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        map = {}
        for string in strs:
            sorted_key = "".join(sorted(string))
            if sorted_key in map:
                string_arr = map.get(sorted_key)
                string_arr.append(string)
                map[sorted_key] = string_arr
            else:
                map[sorted_key] = [string]

        for arr in map.values():
            result.append(arr)
        return result

        