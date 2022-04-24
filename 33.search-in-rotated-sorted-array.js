/*
 * @lc app=leetcode id=33 lang=javascript
 *
 * [33] Search in Rotated Sorted Array
 */
/**
 * integer array ascending order
 * 二分法
 * 
 * 4,5,6,7,0,1,2
 * 乱序的条件 左侧元素 > 右侧元素
 */
// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {

  let l = 0, r = nums.length - 1;
  while (l <= r) {
    let mid = l + ((r - l) >> 1)

    if (targe === nums[mid]) {
      return mid
    }

    if (nums[mid] >= nums[l]) {
      if (nums[l] <= target && nums[mid] > target) {
        r = mid - 1
      } else {
        l = mid + 1
      }
    } else {
      if (nums[mid] < target && nums[r] >= target) {
        l = mid + 1
      } else {
        r = mid - 1
      }

    }
  }
  return -1
};
// @lc code=end

