import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<TreeNode> nodes = new ArrayList<>();
        List<Double> res = new ArrayList<>();
        nodes.add(root);
        while (!nodes.isEmpty()) {
            List<TreeNode> nextLevel = new ArrayList<>();
            double avg = 0;
            for (TreeNode node : nodes) {
                avg += node.val;
                if (node.left != null) {
                    nextLevel.add(node.left);
                }
                if (node.right != null) {
                    nextLevel.add(node.right);
                }
            }
            res.add(avg / nodes.size());
            nodes = nextLevel;
        }
        return res;
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
