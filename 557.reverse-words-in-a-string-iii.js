/*
 * @lc app=leetcode id=557 lang=javascript
 *
 * [557] Reverse Words in a String III
 */

// @lc code=start
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  if (!s) {
    return s
  }
  let ans = s.split(' ').map(item => reverseStr(item))

  return ans.join(' ')

  function reverseStr(str) {
    let arr = []
    for (let i = 0; i < str.length; i++) {
      arr.unshift(str[i])
    }
    return arr.join('')
  }
};
// @lc code=end

