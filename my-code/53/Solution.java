class Solution {
    public static void main(String[] args) {
        System.out.println(new Solution().maxSubArray(new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 }));
    }

    public int maxSubArray(int[] nums) {
        int sum = 0;
        int max = Integer.MIN_VALUE;
        for (int x : nums) {
            sum += x;
            max = Math.max(sum, max);
            sum = Math.max(sum, 0);
        }
        return max;
    }
}
