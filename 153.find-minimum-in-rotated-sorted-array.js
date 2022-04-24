/*
 * @lc app=leetcode id=153 lang=javascript
 *
 * [153] Find Minimum in Rotated Sorted Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  if (!nums || !nums.length) {
    return
  }
  let l = 0, r = nums.length - 1, mid = null;
  while (l <= r) {
    mid = l + (r - l) >> 1
    if (nums[mid] > nums[0]) {
      l = mid + 1
    } else if (nums[mid] < nums[r]) {
      r = mid - 1
    }

    if (nums[mid] > nums[mid + 1]) {
      return nums[mid + 1]
    }
    if (nums[mid] < nums[mid - 1]) {
      return nums[mid - 1]
    }

  }
};
// @lc code=end

