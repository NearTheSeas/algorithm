/*
 * @lc app=leetcode id=68 lang=javascript
 *
 * [68] Text Justification
 */

// @lc code=start
/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function (words, maxWidth) {

  const ans = []
  let pointer = 0, n = words.length
  while (true) {

    const start = pointer // 起始位置 用于单词截取
    let sumLen = 0 // 统计当前行的长度
    while (pointer < n && sumLen + words[pointer].length + pointer - start <= maxWidth) {
      sumLen += words[pointer].length
      pointer++
    }

    // 最后一行
    if (pointer === n) {
      const s = words.slice(start).join(' ')
      ans.push(s + blank(maxWidth - s.length))
      break
    }

    const numWords = pointer - start
    const numSpaces = maxWidth - sumLen

    if (numWords === 1) {
      ans.push(words[start] + blank(numSpaces))
      continue
    }

    const avgSpaces = Math.floor(numSpaces / (numWords - 1))
    const extraSpaces = numSpaces % (numWords - 1)
    // 如果空行不能均分，前面的词空格需要增加
    const str1 = words.slice(start, start + extraSpaces + 1).join(blank(avgSpaces + 1));
    const str2 = words.slice(start + extraSpaces + 1, pointer).join(blank(avgSpaces)); // 拼接其余单词
    ans.push(str1 + blank(avgSpaces) + str2);
  }
  return ans
};

const blank = (n) => {
  return new Array(n).fill(" ").join('')
}
// @lc code=end

