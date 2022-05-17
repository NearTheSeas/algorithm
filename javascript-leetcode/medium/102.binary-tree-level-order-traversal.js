/*
 * @lc app=leetcode id=102 lang=javascript
 *
 * [102] Binary Tree Level Order Traversal
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
 * @return {number[][]}
 */
var levelOrder = function (root) {
  if (!root) {
    return []
  }
  let ans = []
  let stack = [root]
  while (stack.length) {
    let levelStack = [], tmpAns = []
    while (stack.length) {
      let cur = stack.shift()
      tmpAns.push(cur.val)
      if (cur.left) levelStack.push(cur.left)
      if (cur.right) levelStack.push(cur.right)
    }
    ans.push(tmpAns)
    stack = levelStack
  }
  return ans
};
// @lc code=end

