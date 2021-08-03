// @Time     : 2021/05/28 17: 47
// @Author   : Ranshi
// @File     : 9. 回文数.js

/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = function (x) {
    let ch = String(x)
    for (let i = 0, j = ch.length - 1; i <= j; i++, j--) {
        if (ch[i] !== ch[j]) {
            return false
        }
    }
    return true
};


console.log(isPalindrome(x = 121));