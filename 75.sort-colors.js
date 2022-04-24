/*
 * @lc app=leetcode id=75 lang=javascript
 *
 * [75] Sort Colors
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {

  // 两次循环，第一次处理 0， 第二次处理 1
  // let len = nums.length, pointer = 0
  // for (let i = 0; i < len; i++) {
  //   if (nums[i] == 0) {
  //     let tmp = nums[i]
  //     nums[i] = nums[pointer]
  //     nums[pointer++] = tmp
  //   }
  // }

  // for (let i = pointer; i < len; i++) {
  //   if (nums[i] == 1) {
  //     let tmp = nums[i]
  //     nums[i] = nums[pointer]
  //     nums[pointer++] = tmp
  //   }
  // }

  // 单循环 双指针 p0存储0的位置 p2存储2的位置
  let len = nums.length, p0 = 0, p2 = len - 1
  for (i = 0; i <= p2; i++) {
    while (i <= p2 && nums[i] == 2) {
      let tmp = nums[i]
      nums[i] = nums[p2]
      nums[p2] = tmp
      p2 -= 1
    }
    if (nums[i] == 0) {
      let tmp = nums[i]
      nums[i] = nums[p0]
      nums[p0++] = tmp
    }
  }

};
// @lc code=end

