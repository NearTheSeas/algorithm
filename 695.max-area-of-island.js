/*
 * @lc app=leetcode id=695 lang=javascript
 *
 * [695] Max Area of Island
 */

// @lc code=start
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function (grid) {
  let m = grid.length
  let n = grid[0].length
  let ans = 0
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      ans = Math.max(ans, traverse(i, j))
    }
  }
  return ans

  function traverse(i, j) {
    if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] !== 1) {
      return 0
    }
    grid[i][j] = 2
    let areas = 1
    let directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    directions.forEach(([x, y]) => {
      areas += traverse(i + x, j + y)
    });
    return areas
  }
};
// @lc code=end

