/*
 * @lc app=leetcode id=15 lang=javascript
 *
 * [15] 3Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  // length < 3
  // 不能重复 
  // 先排序
  // 固定一个数字，后两个数字头尾进行
  const ans = []
  const len = nums.length;
  if (nums == null || len < 3) return ans;
  nums.sort((a, b) => a - b)
  for (let i = 0; i < len; i++) {
    if (nums[i] > 0) break;
    if (i > 0 && nums[i] === nums[i - 1]) continue
    let left = i + 1, right = len - 1;
    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right]
      if (sum === 0) {
        ans.push([nums[i], nums[left], nums[right]])
        while (left < right && nums[left + 1] === nums[left]) left++
        while (left < right && nums[right - 1] === nums[right]) right--
        left++
        right--
      } else if (sum < 0) {
        left++
      } else if (sum > 0) {
        right--
      }
    }
  }
  return ans
};

// @lc code=end

