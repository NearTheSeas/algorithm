/*
 * @lc app=leetcode id=2 lang=javascript
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {

  let carry = 0, dummy = cur = new ListNode(0)
  while (l1 || l2 || carry) {
    if (l1) {
      carry += l1.val
      l1 = l1.next
    }
    if (l2) {
      carry += l2.val
      l2 = l2.next
    }
    let node = new ListNode(carry % 10)
    carry = ~~(carry / 10)
    cur.next = node
    cur = cur.next
  }
  return dummy.next
};
// @lc code=end

