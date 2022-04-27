/*
 * @lc app=leetcode id=1 lang=javascript
 *
 * [1] Two Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let numMap = new Map()
  for (let i = 0; i < nums.length; i++) {
    let rest = target - nums[i]
    if (numMap.has(rest)) {
      return [numMap.get(rest), i]
    }
    numMap.set(nums[i], i)
  }
  return []
};
// @lc code=end

