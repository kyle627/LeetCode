class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null){  //check if null
            return true;
        }
        if(p != null && q != null){  //recursively check
            return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }
        return false;
    }
}