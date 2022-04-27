/*
 * @lc app=leetcode id=5 lang=javascript
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  let ans = '', strLen = s.length
  for (let i = 0; i < strLen; i++) {
    let s1 = centerSpread(s, i, i)
    let s2 = centerSpread(s, i, i + 1)
    ans = ans.length > s1.length ? ans : s1;
    ans = ans.length > s2.length ? ans : s2;

  }
  return ans


  function centerSpread(s, i, j) {
    while (i >= 0 && j < strLen && s[i] == s[j]) {
      i--
      j++
    }
    return s.substr(i + 1, j - i - 1)
  }
};
// @lc code=end

