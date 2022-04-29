/*
 * @lc app=leetcode id=168 lang=javascript
 *
 * [168] Excel Sheet Column Title
 */

// @lc code=start
/**
 * @param {number} columnNumber
 * @return {string}
 */
var convertToTitle = function(columnNumber) {
    
  let  ans = []
  while (columnNumber > 0) {
    columnNumber --
    ans.unshift(String.fromCharCode(columnNumber % 26 + 65))
    columnNumber = ~~( columnNumber/26)
  }
  return ans.join('')
};
// @lc code=end

