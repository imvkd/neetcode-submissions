class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for(String s: strs) {
            res.append(s.length())
                .append("#")
                .append(s);
        }
        // System.out.print(res.toString());
        return res.toString();
    }

    public List<String> decode(String str) {
        int i = 0;
        List<String> res = new ArrayList<>();
        while(i < str.length()) {
            int j = i+1;
            while(str.charAt(j) != '#') {
                j++;
            }
            // System.out.println(i + "--" + j);
            int length = Integer.parseInt(str.substring(i, j));
            i = j + 1;
            j = i + length;
            String word = str.substring(i, j);
            res.add(word);
            i = j;
        }
        return res;
    }
}
