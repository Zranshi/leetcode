import java.util.ArrayList;
import java.util.List;

public class Solution {
    List<Integer> vals;
    List<Integer> numbers;

    public int sumNumbers(TreeNode root) {
        vals = new ArrayList<>();
        numbers = new ArrayList<>();
        dfs(root);
        int res = 0;
        for (Integer i : numbers) {
            res += i;
        }
        return res;
    }

    public void dfs(TreeNode node) {
        vals.add(node.val);
        if (node.left == null && node.right == null) {
            int number = 0;
            for (Integer val : vals) {
                number *= 10;
                number += val;
            }
            numbers.add(number);
        }
        if (node.left != null) {
            dfs(node.left);
        }
        if (node.right != null) {
            dfs(node.right);
        }
        vals.remove(vals.size() - 1);
    }

}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
