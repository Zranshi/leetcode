// @Time     : 2021/05/28 17: 47
// @Author   : Ranshi
// @File     : 141. 环形链表.js
function ListNode(val) {
    this.val = val
    this.next = null
}

/**
 * @param {ListNode} head
 * @return {boolean}
 */
const hasCycle = function (head) {
    while (head) {
        if (head.tag) {
            return true
        }
        head.tag = true
        head = head.next
    }
    return false
};


console.log(head = [3, 2, 0, -4], pos = 1)