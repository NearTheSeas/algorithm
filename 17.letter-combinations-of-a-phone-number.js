/*
 * @lc app=leetcode id=17 lang=javascript
 *
 * [17] Letter Combinations of a Phone Number
 */

// @lc code=start
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {

  let phoneMap = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
  }


  function backtrack(index) {
    if (index === digits.length) {
      ans.push(curArr.join(''))
    } else {
      let digit = digits[index]
      for (let char of phoneMap[digit]) {
        curArr.push(char)
        backtrack(index + 1)
        curArr.pop()
      }
    }

  }

  let ans = [], curArr = []
  backtrack(0)
  return ans
};
// @lc code=end

