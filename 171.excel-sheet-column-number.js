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
var titleToNumber = function(columnTitle) {
  let n = columnTitle.length
  let ans = 0
  for(let i=0;i<n;i++) {
    ans = ans*26 + (columnTitle[i].charCodeAt() - 'A'.charCodeAt() + 1)
  }
  return ans
};
// @lc code=end

