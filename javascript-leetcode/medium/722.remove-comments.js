/*
 * @lc app=leetcode id=722 lang=javascript
 *
 * [722] Remove Comments
 */

// @lc code=start
/**
 * @param {string[]} source
 * @return {string[]}
 */
var removeComments = function(source) {
    let inBlock = false
    let ans = []
    let newLine = []
    
    for (let line of source) {
      let i = 0
      if (!inBlock) newLine = []

      while (i < line.length) {
        const ch = line[i]
        if(ch === '/' && line[i+1] === '*' && !inBlock) {
          inBlock = true
          i += 1
        }else if (ch === '*' && line[i+1] === '/' && inBlock) {
          inBlock = false
          i += 1
        } else if (!inBlock && ch === '/' && line[i+1] === '/') {
          break
        } else if (!inBlock) {
          newLine.push(line[i])
        }
        i += 1
      }
      if (newLine.length && !inBlock) {
        ans.push(newLine.join(''))
      }
    }
    return ans
};
// @lc code=end

