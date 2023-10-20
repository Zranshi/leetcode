public class Solution {
    public static void main(String[] args) {
        System.out.println(new Solution().canCompleteCircuit(new int[] { 1, 2, 3, 4, 5 }, new int[] { 3, 4, 5, 1, 2 }));
    }

    public int canCompleteCircuit(int[] gas, int[] cost) {
        int[] diff = new int[gas.length];
        int total = 0;
        for (int i = 0; i < diff.length; i++) {
            diff[i] = gas[i] - cost[i];
            total += diff[i];
        }
        if (total < 0) {
            return -1;
        }
        int start = 0, money = 0;
        for (int i = 0; i < diff.length; i++) {
            money += diff[i];
            if (money < 0) {
                start = i + 1;
                money = 0;
            }
        }
        return start;
    }
}
