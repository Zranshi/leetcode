import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println(new Solution().findMinArrowShots(new int[][] {
                { 1, 2 },
                { 3, 4 },
                { 5, 6 },
                { 7, 8 },
        }));
    }

    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (o1, o2) -> {
            if (o1[0] == o2[0]) {
                return o1[1] - o2[1];
            }
            return o1[0] - o2[0];
        });
        ArrayList<int[]> arrowsList = new ArrayList<>();
        for (int[] point : points) {
            if (arrowsList.size() == 0) {
                arrowsList.add(point);
            }
            int[] peekArrow = arrowsList.get(arrowsList.size() - 1);
            if (peekArrow[0] <= point[1] && peekArrow[1] >= point[0]) {
                peekArrow[0] = Math.max(peekArrow[0], point[0]);
                peekArrow[1] = Math.min(peekArrow[1], point[1]);
            } else {
                arrowsList.add(point);
            }
        }
        return arrowsList.size();
    }
}
