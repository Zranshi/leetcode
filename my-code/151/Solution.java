import java.util.StringJoiner;

public class Solution {
    public static void main(String[] args) {
        System.out.println(new Solution().reverseWords("the sky is blue"));
    }

    public String reverseWords(String s) {
        String[] words = s.split(" ");
        for (int i = 0; i < words.length / 2; i++) {
            String w = words[i];
            words[i] = words[words.length - i - 1];
            words[words.length - i - 1] = w;
        }
        var sj = new StringJoiner(" ");
        for (String word : words) {
            if (!word.isBlank()) {
                sj.add(word);
            }
        }
        return sj.toString();
    }
}
