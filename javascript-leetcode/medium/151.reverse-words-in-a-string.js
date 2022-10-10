/*
 * @lc app=leetcode id=151 lang=javascript
 *
 * [151] Reverse Words in a String
 */

// @lc code=start
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
   let left =0, right=s.length -1
   while (left <= right && s[left] === ' '){
    left += 1
   }
   while (left <= right && s[right] === ' ' ){
    right -=1
   }

   let ans = [], word = []
   while (left <= right) {s
    if(s[left] === ' ' && word.length) {
      ans.unshift(word.join(''))
      word = []
    }else if(s[left] !== ' '){
      word.push(s[left])
    }
    left += 1
   }
   ans.unshift(word.join(''))
   return ans.join(' ')
};
// @lc code=end
