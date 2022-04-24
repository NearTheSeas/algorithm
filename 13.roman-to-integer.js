/*
 * @lc app=leetcode id=13 lang=javascript
 *
 * [13] Roman to Integer
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  let numMap = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
  let ans = 0
  for (let i = 0; i < s.length; i++) {
    if (i < s.length - 1 && numMap[s[i]] < numMap[s[i + 1]]) {
      ans -= numMap[s[i]]
    } else {
      ans += numMap[s[i]]
    }
  }
  return ans
};
// @lc code=end

