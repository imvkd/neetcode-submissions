class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0;
        int res = 0;
        Set<Character> charSet = new HashSet<>();

        for(int j = 0; j<s.length(); j++) {
            while(charSet.contains(s.charAt(j))) {
                // System.out.println(charSet);
                charSet.remove(s.charAt(i));
                // System.out.println(charSet);
                i++;
            }
            charSet.add(s.charAt(j));
            res = Math.max(res, j-i+1);
        }
        return res;
    }
}
