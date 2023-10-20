public class Solution {
    public static void main(String[] args) {
        System.out.println(new Solution().minSubArrayLen(4, new int[] { 1, 4, 4 }));
    }

    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, right = 0, sum = 0, res = Integer.MAX_VALUE;
        while (right < nums.length) {
            sum += nums[right];
            while (sum - nums[left] >= target) {
                sum -= nums[left];
                left++;
            }
            if (sum >= target) {
                res = Math.min(right - left + 1, res);
            }
            right++;
        }
        return res == Integer.MAX_VALUE ? 0 : res;
    }
}
