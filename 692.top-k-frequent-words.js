/*
 * @lc app=leetcode id=692 lang=javascript
 *
 * [692] Top K Frequent Words
 */

// @lc code=start
/**
 * @param {string[]} words
 * @param {number} k
 * @return {string[]}
 */
var topKFrequent = function (words, k) {
  let cnt = new Map()
  for (let word of words) {
    cnt.set(word, (cnt.get(word) || 0) + 1)
  }
  let arr = []
  for (let word of cnt.keys()) {
    arr.push(word)
  }

  arr.sort((word1, word2) => {
    let cnt1 = cnt.get(word1),
      cnt2 = cnt.get(word2)

    return cnt1 === cnt2 ? word1.localeCompare(word2) : cnt2 - cnt1
  })

  return arr.slice(0, k)
};
// @lc code=end

