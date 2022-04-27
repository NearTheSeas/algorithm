/*
 * @lc app=leetcode id=54 lang=javascript
 *
 * [54] Spiral Matrix
 */

// @lc code=start
/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  if (!matrix || !matrix.length) {
    return []
  }
  let top = 0, bottom = matrix.length - 1, left = 0, right = matrix[0].length - 1;
  let ans = []
  while (true) {
    for (let i = left; i <= right; i++) {
      ans.push(matrix[top][i])
    }
    top += 1
    if (top > bottom) {
      break
    }

    for (let i = top; i <= bottom; i++) {
      ans.push(matrix[i][right])
    }
    right -= 1
    if (right < left) {
      break
    }

    for (let i = right; i >= left; i--) {
      ans.push(matrix[bottom][i])
    }
    bottom -= 1
    if (bottom < top) {
      break
    }

    for (let i = bottom; i >= top; i--) {
      ans.push(matrix[i][left])
    }
    left += 1
    if (left > right) {
      break
    }
  }
  return ans
};
// @lc code=end

