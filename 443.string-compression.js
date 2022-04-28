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
  let length = chars.length
    let prev = chars[0], pos = 0, counter = 0
    for (let i = 0; i < length; i++) {
        let cur = chars[i]
        if (cur != prev) {
            chars[pos++] = prev

            if (counter > 1) {
                for (let digit of counter.toString()) {
                    chars[pos++] = (digit)
                }
            }
            prev = cur
            counter = 1
        } else {
            counter += 1
        }
    }
    chars[pos++] = prev
    if (counter > 1) {
        for (let digit of counter.toString()) {
            chars[pos++] = (digit)
        }
    }
    chars.length = pos
};
// @lc code=end

