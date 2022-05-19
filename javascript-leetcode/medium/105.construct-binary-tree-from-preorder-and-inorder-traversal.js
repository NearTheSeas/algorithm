/*
 * @lc app=leetcode id=105 lang=javascript
 *
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
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
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
  let idxMap = {}
  inorder.forEach((item, idx) => idxMap[item] = idx)
  /** 
   * 前序遍历 识别根节点 
   * root    [左子树]   [右子树]
   * 
   * 中序遍历 配合前序的根节点，识别左子树
   * [左子树]  root     [右子树] 
   * */
  let len = preorder.length - 1
  const buildNode = (preStart, preEnd, inStart, inEnd) => {
    if (preStart > preEnd) {
      return null
    }

    // 根节点
    const curVal = preorder[preStart]
    const rootNode = new TreeNode(curVal)

    // 再中序遍历中找到根节点位置 进而计算左子树长度 也就是下一个要遍历子树的长度
    const inRootIdx = idxMap[curVal]
    const subSize = inRootIdx - inStart;

    rootNode.left = buildNode(preStart + 1, preStart + subSize, inStart, inRootIdx - 1) //递归
    rootNode.right = buildNode(preStart + subSize + 1, preEnd, inRootIdx + 1, inEnd) //递归

    return rootNode
  }

  return buildNode(0, len, 0, len)
};
// @lc code=end

