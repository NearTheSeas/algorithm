/*
 * @lc app=leetcode id=23 lang=javascript
 *
 * [23] Merge k Sorted Lists
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
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {

  let ans = null
  for (let i = 0; i < lists.length; i++) {
    ans = mergeTwo(ans, lists[i])
  }

  return ans

  function mergeTwo(l1, l2) {
    if (!l1) {
      return l2
    }

    if (!l2) {
      return l1
    }
    let head = cur = new ListNode(0)

    while (l1 && l2) {
      if (l1.val <= l2.val) {
        cur.next = l1
        l1 = l1.next
      } else {
        cur.next = l2
        l2 = l2.next
      }
      cur = cur.next
    }

    if (l1) {
      cur.next = l1
    }
    if (l2) {
      cur.next = l2
    }

    return head.next
  }

};
// @lc code=end

