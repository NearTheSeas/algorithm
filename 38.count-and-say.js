/*
 * @lc app=leetcode id=38 lang=javascript
 *
 * [38] Count and Say
 */

// @lc code=start
/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function (n) {
  let str = '1'
  for (let i = 2; i <= n; i++) {
    const strArr = []
    let start = 0
    let pos = 0

    while (pos < str.length) {
      while (pos < str.length && str[pos] === str[start]) {
        pos++
      }
      strArr.push("" + (pos - start) + str[start])
      start = pos
    }
    str = strArr.join('')
  }
  return str
};
// @lc code=end

