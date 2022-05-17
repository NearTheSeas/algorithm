/*
 * @lc app=leetcode id=79 lang=javascript
 *
 * [79] Word Search
 */

// @lc code=start
/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
  let m = board.length, n = board[0].length

  const traverse = (row, col, idx) => {
    if (board[row][col] !== word.charAt(idx)) {
      return false
    } else if (idx === word.length - 1) {
      return true
    }
    let before = board[row][col]
    let tmp = false
    board[row][col] = '#'
    for (let [x, y] of [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]) {
      if (x >= 0 && x < m && y >= 0 && y < n) {
        tmp = traverse(x, y, idx + 1)
        if (tmp) {
          tmp = true
          break
        }
      }
    }
    board[row][col] = before
    return tmp
  }

  let ans = false
  for (let row = 0; row < m; row++) {
    for (let col = 0; col < n; col++) {
      ans = traverse(row, col, 0)
      if (ans) {
        return true
      }
    }
  }
  return ans
};
// @lc code=end

