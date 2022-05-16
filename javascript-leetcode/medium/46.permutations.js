/*
 * @lc app=leetcode id=46 lang=javascript
 *
 * [46] Permutations
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
  // 全排列 回溯
  let ans = [], path = []
  let len = nums.length

  const traverse = (nums, len, curArr, used) => {
    if (curArr.length === len) {
      ans.push([...curArr])
      return
    }

    for (let i = 0; i < len; i++) {
      if (used[i]) continue
      curArr.push(nums[i])
      used[i] = true
      traverse(nums, len, curArr, used)
      curArr.pop()
      used[i] = false
    }
  }

  traverse(nums, len, path, [])
  return ans
};
// @lc code=end

