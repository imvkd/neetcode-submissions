class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, ArrayList> res = new HashMap<>();
        for(String s : strs) {
            int[] count = new int[26];
            for(char c : s.toCharArray()) {
                count[c - 'a']++;
            }
            String cnt = Arrays.toString(count);
            res.putIfAbsent(cnt, new ArrayList<String>());
            res.get(cnt).add(s);
        }

        return new ArrayList(res.values());
    }
}
