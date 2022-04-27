/*
 * @lc app=leetcode id=443 lang=javascript
 *
 * [443] String Compression
 */

// @lc code=start
/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function (chars) {
  console.log(chars)
  let length = chars.length
  let prev = null, pos = 0
  for (let i = 0; i < length; i++) {
    let cur = chars.unshift()
    console.log(cur)
    if (prev || cur != prev) {
      chars.push(prev)
      let len = (i - pos + 1)
      if (len > 1) {
        chars.push(len)
      }

      prev = cur
      pos = i
    }
  }
  console.log(chars)

  chars.length
};
// @lc code=end

