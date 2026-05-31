class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length())
            return false;

        HashMap<Character, Integer> c1 = new HashMap<>();
        HashMap<Character, Integer> c2 = new HashMap<>();

        for(int i=0; i<s.length(); i++) {
            c1.put(s.charAt(i), c1.getOrDefault(s.charAt(i), 0)+1);
            c2.put(t.charAt(i), c2.getOrDefault(t.charAt(i), 0) +1);
        }
        return c1.equals(c2);
    }
}
