class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();

        for(Integer num : nums) {
            map.put(num, 1 + map.getOrDefault(num, 0));
            if(map.get(num) > 1) {
                // System.out.println(num);
                return true;
            }
        }
        return false;
    }
}