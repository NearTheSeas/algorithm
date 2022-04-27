/*
 * @lc app=leetcode id=133 lang=javascript
 *
 * [133] Clone Graph
 */

// @lc code=start
/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function (node) {
  if (!node) {
    return node
  }
  let nodeMap = new Map()
  let arr = [node]
  nodeMap.set(node, new Node(node.val))

  while (arr.length) {
    let cur = arr.shift()
    for (let neighbor of cur.neighbors) {
      if (!nodeMap.get(neighbor)) {
        nodeMap.set(neighbor, new Node(neighbor.val))
        arr.push(neighbor)
      }
      nodeMap.get(cur).neighbors.push(nodeMap.get(neighbor))
    }
  }

  return nodeMap.get(node)
};
// @lc code=end

