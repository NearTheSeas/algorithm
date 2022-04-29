/*
 * @lc app=leetcode id=42 lang=javascript
 *
 * [42] Trapping Rain Water
 */

// @lc code=start
/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    // 利用堆栈 记录柱体高度
    // 可以存水的时候 累计
    // 合适记录和出入栈？
    let stack = [], ans = 0, n = height.length
    for(let i=0;i<n;i++){
      while(stack.length && height[i] > height[stack[stack.length-1]]) {
        const top = stack.pop()
        if(!stack.length) {
          break
        }
        const left = stack[stack.length-1]
        const curWidth = i-left -1
        const curHeight = Math.min(height[left], height[i]) - height[top]
        ans += curWidth*curHeight
      }
      stack.push(i)
    }
 
    return ans
};
// @lc code=end

