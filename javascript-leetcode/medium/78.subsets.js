/*
 * @lc app=leetcode id=78 lang=javascript
 *
 * [78] Subsets
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
  const ans = []
  const traverse = (idx, path) => {
    ans.push([...path])
    for (let i = idx; i < nums.length; i++) {
      path.push(nums[i])
      traverse(i + 1, path)
      path.pop()
    }
  }

  traverse(0, [])
  return ans
};
// @lc code=end

