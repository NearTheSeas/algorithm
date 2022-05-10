/*
 * @lc app=leetcode id=268 lang=javascript
 *
 * [268] Missing Number
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
 var missingNumber = function (nums) {
  let ans = 0
  let n = nums.length
  for (let num of nums) {
      ans ^= num
  }
  for (let i = 0; i <= n; i++) {
      ans ^= i
  }
  return ans
};
// @lc code=end

