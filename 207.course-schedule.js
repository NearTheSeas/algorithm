/*
 * @lc app=leetcode id=207 lang=javascript
 *
 * [207] Course Schedule
 */

// @lc code=start
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {

    let indegrees = new Array(numCourses).fill(0)
    let adjacency = new Array(numCourses).fill([])

    for (let item of prerequisites) {
      const [cur, pre] = item
      indegrees[cur] += 1
      adjacency[pre] = [...adjacency[pre], cur]
    }
    
    let queen = []
    for(let i=0;i<indegrees.length;i++) {
        if(indegrees[i] === 0) {
          queen.push(i)
        }
    }

    while(queen.length) {
      let pre = queen.shift()
      numCourses --
      for(let cur of adjacency[pre]){
        indegrees[cur] -=1
        if(!indegrees[cur]) {
          queen.push(cur)
        }
      }
    }
    return !numCourses
};
// @lc code=end

