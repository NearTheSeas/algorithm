/*
 * @lc app=leetcode id=4 lang=javascript
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  /**
   * 有序数组 → 二分法
   * 区分总数奇偶
   */
  const findKthElement = (k) => {
    let index1 = 0, index2 = 0
    while (true) {
      if (index1 === m) {
        return nums2[index2 + k - 1]
      }
      if (index2 === n) {
        return nums1[index1 + k - 1]
      }
      if (k === 1) {
        return Math.min(nums1[index1], nums2[index2])
      }

      // 取第 k/2个数，避免溢出
      const newIndex1 = Math.min(index1 + ~~(k / 2) - 1, m - 1)
      const newIndex2 = Math.min(index2 + ~~(k / 2) - 1, n - 1)
      const pos1 = nums1[newIndex1]
      const pos2 = nums2[newIndex2]
      if (pos1 <= pos2) {
        k -= newIndex1 - index1 + 1
        index1 = newIndex1 + 1
      } else {
        k -= newIndex2 - index2 + 1
        index2 = newIndex2 + 1
      }
    }
  }

  const m = nums1.length
  const n = nums2.length
  const total = m + n
  // 奇数直接返回中位数
  if (total % 2 === 1) {
    return findKthElement(~~((total + 1) / 2))
  } else {
    // 偶数需要得到 k 和 k+1 
    return (findKthElement(total / 2) + findKthElement(total / 2 + 1)) / 2
  }
};
// @lc code=end

