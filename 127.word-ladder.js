/*
 * @lc app=leetcode id=127 lang=javascript
 *
 * [127] Word Ladder
 */

// @lc code=start
/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function (beginWord, endWord, wordList) {
  let begins = [beginWord], ends = [endWord], wordSet = new Set(wordList)
  if (!wordSet.has(endWord)) {
    return 0
  }
  let wordLen = beginWord.length
  let steps = 1
  while (begins.length) {

    steps += 1
    let tmpArr = []
    for (let curWord of begins) {
      for (let i = 0; i < wordLen; i++) {
        for (let c of 'abcdefghijklmnopqrstuvwxyz') {
          let newWord = curWord.slice(0, i) + c + curWord.slice(i + 1);
          if (ends.includes(newWord)) {
            return steps
          }
          if (wordSet.has(newWord)) {
            tmpArr.push(newWord)
            wordSet.delete(newWord)
          }
        }
      }
    }
    begins = tmpArr
    if (begins.length > ends.length) {
      let tmp = ends
      ends = begins
      begins = tmp
    }

  }
  return 0
};
// @lc code=end

