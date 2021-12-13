// @Time     : 2021/05/28 17: 46
// @Author   : Ranshi
// @File     : 2. 两数相加.js
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = function (l1, l2) {
  const l3 = new ListNode(0);
  let p1 = l1,
    p2 = l2,
    p3 = l3,
    carry = 0;
  while (p1 || p2) {
    const v1 = p1 ? p1.val : 0,
      v2 = p2 ? p2.val : 0,
      val = v1 + v2 + carry;
    carry = Math.floor(val / 10);
    p3.next = new ListNode(val % 10);
    if (p1) {
      p1 = p1.next;
    }
    if (p2) {
      p2 = p2.next;
    }
    p3 = p3.next;
  }
  if (carry) {
    p3.next = new ListNode(carry);
  }
  return l3.next;
};
