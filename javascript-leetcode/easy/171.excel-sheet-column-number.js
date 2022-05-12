/*
 * @lc app=leetcode id=171 lang=javascript
 *
 * [171] Excel Sheet Column Number
 */

// @lc code=start
/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function (columnTitle) {
  let ans = 0
  for (let ch of columnTitle) {
    ans = ans * 26 + ch.charCodeAt() - 'A'.charCodeAt() + 1
  }
  return ans
};
// @lc code=end

