public class Solution {
    int res = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return res;
    }

    int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int leftValue = dfs(node.left);
        int rightValue = dfs(node.right);
        int subMax = node.val + Math.max(0, Math.max(leftValue, rightValue));
        res = Math.max(Math.max(node.val + leftValue + rightValue, subMax), res);
        return subMax;
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
