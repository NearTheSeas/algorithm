/*
 * @lc app=leetcode id=3 lang=javascript
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  let ans = 0
  let curArr = []
  for(let ch of Array.from(s)) {
    while(curArr.includes(ch)) {
      curArr.shift()
    }
    curArr.push(ch)
    ans = Math.max(curArr.length, ans)
  }
  return ans
};
// @lc code=end

