/*
 * @lc app=leetcode id=53 lang=javascript
 *
 * [53] Maximum Subarray
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let ans = nums[0], cur = 0
    for(let num of nums) {
      cur += num
      ans = Math.max(cur, ans)
      if(cur <= 0) {
        cur = 0
      }
    }
    return ans
};
// @lc code=end

