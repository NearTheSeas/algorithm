/*
 * @lc app=leetcode id=215 lang=javascript
 *
 * [215] Kth Largest Element in an Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function (nums, k) {

  const quick = (l, r) => {
    if (l > r) return
    let random = Math.floor(Math.random() * (r - l + 1)) + l
    swap(nums, r, random)

    const pivotIndex = partition(nums, l, r)
    if (n - k < pivotIndex) {
      quick(l, pivotIndex - 1)
    } else {
      quick(pivotIndex + 1, r)
    }
  }

  const n = nums.length
  quick(0, n - 1)
  return nums[n - k]
};

function partition(nums, left, right) {
  const pivot = nums[right]
  let pivotIndex = left
  for (let i = left; i < right; i++) {
    if (nums[i] < pivot) {
      swap(nums, i, pivotIndex)
      pivotIndex++
    }
  }
  swap(nums, right, pivotIndex)
  return pivotIndex
}

function swap(nums, p, q) {
  const tmp = nums[p]
  nums[p] = nums[q]
  nums[q] = tmp
}

// @lc code=end

