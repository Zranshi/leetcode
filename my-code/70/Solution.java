public class Solution {
    public static void main(String[] args) {
        System.out.println(new Solution().climbStairs(2));
    }

    public int climbStairs(int n) {
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[0] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}