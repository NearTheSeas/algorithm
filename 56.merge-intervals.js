/*
 * @lc app=leetcode id=56 lang=javascript
 *
 * [56] Merge Intervals
 */

// @lc code=start
/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  let ans = []
  intervals.sort((a, b) => a[0] - b[0])
  for (let interval of intervals) {
    let [newStart, newEnd] = interval
    if (!ans.length || newStart > ans[ans.length - 1][1]) {
      ans.push(interval)
    } else {
      ans[ans.length - 1][1] = Math.max(ans[ans.length - 1][1], newEnd)
    }
  }
  return ans
};
// @lc code=end

