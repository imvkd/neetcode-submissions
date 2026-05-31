class Solution {
    public int lengthOfLongestSubstring(String s) {
        int j = 0;
        int res = 0;
        Set<Character> charSet = new HashSet<>();

        for(int i = 0; i<s.length(); i++) {
            while(charSet.contains(s.charAt(i))) {
                charSet.remove(s.charAt(j));
                j++;
            }
            charSet.add(s.charAt(i));
            res = Math.max(res, i-j+1);
        }
        return res;
    }
}
