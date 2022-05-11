/*
 * @lc app=leetcode id=14 lang=javascript
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  if (!strs.length) {
    return ""
  }
  let len = strs[0].length
  for (let str of strs) {
    len = Math.min(len, str.length)
  }
  let ans = ""
  for (let i = 0; i < len; i++) {
    for (let n = 1; n < strs.length; n++) {
      if (strs[n].charAt(i) != strs[0].charAt(i)) {
        return ans
      }
    }
    ans += strs[0].charAt(i)
  }
  return ans
};
// @lc code=end

