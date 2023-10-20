public class Solution {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.productExceptSelf(new int[] { -1, 1, 0, -3, 3 }));
    }

    public int[] productExceptSelf(int[] nums) {
        int zeroCount = 0;
        int mulTotal = 1;
        int[] res = new int[nums.length];
        for (int i : nums) {
            if (i == 0) {
                zeroCount++;
            } else {
                mulTotal *= i;
            }
        }
        if (zeroCount > 1) {
            return res;
        }
        for (int i = 0; i < res.length; i++) {
            if (zeroCount > 0) {
                if (nums[i] == 0) {
                    res[i] = mulTotal;
                }
            } else {
                res[i] = mulTotal / nums[i];
            }
        }
        return res;
    }
}
