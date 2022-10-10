/*
 * @lc app=leetcode id=235 lang=javascript
 *
 * [235] Lowest Common Ancestor of a Binary Search Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    if (root.val < p.val && root.val < q.val) {
      return lowestCommonAncestor(root.right, p, q)
    }

    if (root.val > p.val && root.val > q.val) {
      return lowestCommonAncestor(root.left, p, q)
    }

    return root
};
// @lc code=end

