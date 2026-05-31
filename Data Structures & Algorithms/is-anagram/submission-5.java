class Solution {
    public boolean isAnagram(String s, String t) {
        int count[] = new int[26];

        if(s.length() != t.length()) {
            return false;
        }

        int i = 0;
        while(i < s.length()) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
            i++;
        }

        for(int value : count) {
            if(value > 0 ) {
                return false;
            }
        }

        return true;

    }
}
