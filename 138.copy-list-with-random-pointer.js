/*
 * @lc app=leetcode id=138 lang=javascript
 *
 * [138] Copy List with Random Pointer
 */

// @lc code=start
/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function (head) {
  if (!head) {
    return head
  }

  let cur = head
  while (cur) {
    let newNode = new Node(cur.val, cur.next, null)
    cur.next = newNode
    cur = newNode.next
  }

  cur = head
  while (cur) {
    if (cur.random) {
      cur.next.random = cur.random.next
    }
    cur = cur.next.next
  }

  let dummy = cur = new Node(0)
  while (head) {
    cur.next = head.next
    cur = cur.next
    head.next = cur.next
    head = head.next
  }
  return dummy.next
};
// @lc code=end

