/*
 * @lc app=leetcode id=7 lang=javascript
 *
 * [7] Reverse Integer
 */

// @lc code=start
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  let ans = 0
  while (x != 0) {
    let digit = x % 10
    x = ~~(x / 10)
    ans = ans * 10 + digit;
    if (ans < Math.pow(-2, 31) || ans > Math.pow(2, 31) - 1) {
      return 0;
    }
  }
  return ans
};
// @lc code=end

