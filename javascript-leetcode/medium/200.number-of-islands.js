/*
 * @lc app=leetcode id=200 lang=javascript
 *
 * [200] Number of Islands
 */

// @lc code=start
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  if (!grid || !grid[0]) {
    return 0
  }

  const traverse = (row, col) => {
    if (!grid[row][col]) {
      return
    }
    grid[row][col] = 0
    for (let [x, y] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
      let newRow = row + x, newCol = col + y
      if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n && grid[newRow][newCol] === '1') {
        traverse(newRow, newCol)
      }
    }
  }
  let ans = 0
  let m = grid.length, n = grid[0].length
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === '1') {
        ans += 1
        traverse(i, j)
      }
    }
  }
  return ans
};
// @lc code=end

