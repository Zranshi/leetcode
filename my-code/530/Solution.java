public class Solution {
    int res = Integer.MAX_VALUE;
    int tmp = Integer.MAX_VALUE;

    public int getMinimumDifference(TreeNode root) {
        dfs(root);
        return res;
    }

    void dfs(TreeNode node) {
        if (node == null) {
            return;
        }
        dfs(node.left);
        res = Math.min(Math.abs(tmp - node.val), res);
        tmp = node.val;
        dfs(node.right);
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
