/*
 * @lc app=leetcode id=49 lang=javascript
 *
 * [49] Group Anagrams
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  /**
   * 根据字符串生成key 存储再map中
   */
  let strMap = new Map()
  for (let str of strs) {
    const key = str.split('').sort().join()
    let arr = strMap.has(key) ? strMap.get(key) : []
    arr.push(str)
    strMap.set(key, arr)
  }
  return Array.from(strMap.values())
};
// @lc code=end

