/*
 * @lc app=leetcode id=11 lang=javascript
 *
 * [11] Container With Most Water
 */

// @lc code=start
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let i = 0, j = height.length - 1;
  let ans = 0
  while (i < j) {
    ans = Math.max(ans, Math.min(height[i], height[j]) * (j - i))
    if (height[i] <= height[j]) {
      i++
    } else {
      j--
    }
  }
  return ans
};
// @lc code=end

