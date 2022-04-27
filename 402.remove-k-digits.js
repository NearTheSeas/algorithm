/*
 * @lc app=leetcode id=402 lang=javascript
 *
 * [402] Remove K Digits
 */

// @lc code=start
/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var removeKdigits = function (num, k) {
  const stack = []
  for (const digit of num) {
    while (stack.length > 0 && stack[stack.length - 1] > digit && k) {
      stack.pop()
      k -= 1
    }
    stack.push(digit)
  }

  for (; k > 0; --k) {
    stack.pop()
  }

  let ans = ''
  let isLeadingZero = true
  for (const digit of stack) {
    if (isLeadingZero && digit === '0') {
      continue
    }
    isLeadingZero = false
    ans += digit
  }
  return ans === '' ? '0' : ans
};
// @lc code=end

