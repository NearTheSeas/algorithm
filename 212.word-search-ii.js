/*
 * @lc app=leetcode id=212 lang=javascript
 *
 * [212] Word Search II
 */

// @lc code=start
/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
 var findWords = function (board, words) {
  const trie = new Trie()
  for (let word of words) {
      trie.insert(word)
  }
  let ans = new Set()

  const traverse = (row, col, nodes, str) => {
      if (nodes[board[row][col]].isEnd) {
          ans.add(str + board[row][col])
      }
      nodes = nodes[board[row][col]];
      str += board[row][col];
      let tmp = board[row][col]
      board[row][col] = 1
      for (let [newRow, newCol] of [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]) {
          if (
              newRow < 0 ||
              newCol < 0 ||
              newRow >= m ||
              newCol >= n ||
              !nodes[board[newRow][newCol]] ||
              board[newRow][newCol] == 1
          ) continue;

          traverse(newRow, newCol, nodes, str);
      }
      board[row][col] = tmp
  }
  let m = board.length, n = board[0].length;
  for (let row = 0; row < m; row++) {
      for (let col = 0; col < n; col++) {
          if (trie.children[board[row][col]]) {
              traverse(row, col, trie.children, "");
          }
      }
  }
  return [...ans]
};

var Trie = function () {
  this.children = {}
}

Trie.prototype.insert = function (word) {
  let nodes = this.children
  for (let ch of word) {
      if (!nodes[ch]) {
          nodes[ch] = {}
      }
      nodes = nodes[ch]
  }

  nodes.isEnd = true
}

// @lc code=end
