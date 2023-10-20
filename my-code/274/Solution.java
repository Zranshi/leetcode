public class Solution {
    public static void main(String[] args) {
        var s = new Solution();
        int[] citations = { 3, 0, 6, 1, 5 };
        System.out.println(s.hIndex(citations));
    }

    // public int hIndex(int[] citations) {
    // Arrays.sort(citations);
    // int res = 0;
    // for (int i = citations.length - 1; i >= 0; i--) {
    // if (citations[i] >= res + 1) {
    // res++;
    // } else {
    // break;
    // }
    // }
    // return res;
    // }

    public int hIndex(int[] citations) {
        int n = citations.length;
        int[] counter = new int[n + 1];
        for (int i = 0; i < n; i++) {
            if (citations[i] >= n) {
                counter[n]++;
            } else {
                counter[citations[i]]++;
            }
        }
        int res = 0;
        for (int i = n; i >= 0; i--) {
            res += counter[i];
            if (res >= i) {
                return i;
            }
        }
        return 0;
    }
}
