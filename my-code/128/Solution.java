import java.util.HashSet;
import java.util.Set;

class Solution {
    public static void main(String[] args) {
        System.out.println(new Solution().longestConsecutive(new int[] { 100, 4, 200, 1, 3, 2 }));
    }

    public int longestConsecutive(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int i : nums) {
            s.add(Integer.valueOf(i));
        }
        int longestLength = 0;
        for (Integer i : s) {
            if (s.contains(i - 1)) {
                continue;
            }
            int idx = i, idxLength = 0;
            while (s.contains(idx)) {
                idxLength++;
                idx++;
            }
            longestLength = Math.max(idxLength, longestLength);
        }
        return longestLength;
    }
}
