/*
 * @lc app=leetcode id=43 lang=javascript
 *
 * [43] Multiply Strings
 */

// @lc code=start
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function (num1, num2) {
  if (num1 === '0' || num2 === '0') {
    return '0'
  }
  let ans = []
  for (let i = num1.length - 1; i >= 0; i--) {
    for (let j = num2.length - 1; j >= 0; j--) {
      ans[i + j] = (ans[i + j] || 0) + num1[i] * num2[j]
    }
  }

  let carry = 0
  for (let i = ans.length - 1; i >= 0; i--) {
    let cur = ans[i] + carry
    ans[i] = cur % 10
    carry = ~~(cur / 10)
  }
  if (carry) {
    ans.unshift(carry)
  }

  return ans.join('')

};
// @lc code=end

