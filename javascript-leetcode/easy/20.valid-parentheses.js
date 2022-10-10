/*
 * @lc app=leetcode id=20 lang=javascript
 *
 * [20] Valid Parentheses
 */

// @lc code=start
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if(!s){
      return false
    }
    let itemMap = {"(":")","{":"}","[":"]"}
    let stack = []
    for (let item of s){
       if (stack[stack.length -1] === item){
        stack.pop()
      } else {
        stack.push(itemMap[item])
      }
    }
    return stack.length === 0
};
// @lc code=end
