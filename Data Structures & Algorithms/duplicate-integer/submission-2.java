class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for(Integer n : nums){
            if(map.containsKey(n)){
                map.put(n, map.get(n)+1);
            } else {
                map.put(n, 1);
            }
            if (map.get(n) > 1) {
                return true;
            }
        }
        return false;
    }
}