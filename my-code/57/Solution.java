import java.util.ArrayList;

class Solution {
    public static void main(String[] args) {
        int[][] res = new Solution().insert(new int[][] {
                { 1, 3 },
                { 6, 9 },
        }, new int[] { 2, 5 });
        for (int[] is : res) {
            for (int x : is) {
                System.out.print(x);
                System.out.print(' ');
            }
            System.out.println();
        }
    }

    public int[][] insert(int[][] intervals, int[] newInterval) {
        int left = newInterval[0], right = newInterval[1];
        ArrayList<int[]> list = new ArrayList<>();
        boolean isAdded = false;
        for (int i = 0; i < intervals.length; i++) {
            if (isAdded || intervals[i][1] < left) {
                list.add(intervals[i]);
                continue;
            }
            if (intervals[i][0] > right) {
                list.add(new int[] { left, right });
                isAdded = true;
                i--;
            } else if (intervals[i][0] <= right && intervals[i][1] >= left) {
                left = Math.min(left, intervals[i][0]);
                right = Math.max(right, intervals[i][1]);
            }
        }
        if (!isAdded) {
            list.add(new int[] { left, right });
        }
        return list.toArray(new int[list.size()][]);
    }
}
