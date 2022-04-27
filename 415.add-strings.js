/*
 * @lc app=leetcode id=415 lang=javascript
 *
 * [415] Add Strings
 */

// @lc code=start
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function (num1, num2) {
  let m = num1.length - 1, n = num2.length - 1
  let ans = [], carry = 0
  while (m >= 0 || n >= 0 || carry) {
    if (m >= 0) {
      carry += (num1[m] - 0)
      m -= 1
    }
    if (n >= 0) {
      carry += (num2[n] - 0)
      n -= 1
    }
    ans.unshift(carry % 10)
    carry = ~~(carry / 10)
  }
  return ans.join('')

};
// @lc code=end

