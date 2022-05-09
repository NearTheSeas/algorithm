/*
 * @lc app=leetcode id=24 lang=javascript
 *
 * [24] Swap Nodes in Pairs
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * 
 * pre 
 * 1    2         3              4
 * cur cur.next cur.next.next
 * cur.next.next 1-3
 * next.next = cur
 * cur.next = 
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function (head) {

  let newHead = head;
  if (head && head.next) {
    newHead = head.next
  }
  let cur = head, pre = null
  while (cur && cur.next) {
    const next = cur.next
    cur.next = cur.next.next
    next.next = cur
    if (pre) {
      pre.next = next
    }
    pre = cur
    cur = cur.next
  }
  return newHead
};
// @lc code=end

