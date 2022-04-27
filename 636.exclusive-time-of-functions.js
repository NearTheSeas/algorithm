/*
 * @lc app=leetcode id=636 lang=javascript
 *
 * [636] Exclusive Time of Functions
 */

// @lc code=start
/**
 * @param {number} n
 * @param {string[]} logs
 * @return {number[]}
 */
var exclusiveTime = function (n, logs) {
  let ans = new Array(n).fill(0)
  let stack = []
  let prev = 0
  logs.forEach(item => {

    let [id, type, time] = item.split(':')
    time = parseInt(time)

    if (type === 'start') {
      if (stack.length) {
        ans[stack[stack.length - 1]] += (time - prev)
      }
      stack.push(id)
      prev = time
    } else {
      let top = stack.pop()
      ans[top] += (time - prev + 1)

      prev = time + 1
    }
  })

  return ans
};
// @lc code=end


