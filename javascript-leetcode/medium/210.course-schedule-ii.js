/*
 * @lc app=leetcode id=210 lang=javascript
 *
 * [210] Course Schedule II
 */

// @lc code=start
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function (numCourses, prerequisites) {
  /**
   * 构建依赖图
   * 节点的入度
   * 依次遍历没有前置依赖的点
   * 他的后置课程 入度-1  当为0时 加入遍历队列
   */
  let ans = []
  let inDegree = new Array(numCourses).fill(0), courseMap = new Map()
  for (let course of prerequisites) {
    let [cur, pre] = course
    inDegree[cur] += 1
    let list = courseMap.has(pre) ? courseMap.get(pre) : []
    list.push(cur)
    courseMap.set(pre, list)
  }
  let stack = []
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) stack.push(i)
  }
  while (stack.length) {
    let cur = stack.shift()
    ans.push(cur)
    numCourses--
    if (courseMap.has(cur)) {
      for (let course of courseMap.get(cur)) {
        inDegree[course]--
        if (inDegree[course] === 0) stack.push(course)
      }
    }
  }
  return numCourses == 0 ? ans : []
};
// @lc code=end

