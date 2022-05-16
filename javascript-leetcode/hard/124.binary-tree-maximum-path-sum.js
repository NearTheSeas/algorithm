/*
 * @lc app=leetcode id=124 lang=javascript
 *
 * [124] Binary Tree Maximum Path Sum
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function (root) {

  // 二叉树的遍历
  // 求左节点最大值、右节点最大值、根节点最大值
  let ans = Number.MIN_SAFE_INTEGER
  const dfs = (root) => {
    if (!root) {
      return 0
    }
    const maxLeft = Math.max(dfs(root.left), 0)
    const maxRight = Math.max(dfs(root.right), 0)
    const innerMax = root.val + maxLeft + maxRight
    ans = Math.max(ans, innerMax)
    return root.val + Math.max(maxLeft, maxRight)
  }
  dfs(root)
  return ans
};
// @lc code=end

