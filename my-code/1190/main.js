// @Time     : 2021/05/28 17: 47
// @Author   : Ranshi
// @File     : 1190. 反转每对括号间的子串.js
/**
 * @param {string} s
 * @return {string}
 */
const reverseParentheses = function (s) {
    const stk = []
    let str = ''
    for (const ch of s) {
        if (ch === '(') {
            stk.push(str)
            str = ''
        } else if (ch === ')') {
            str = str.split("").reverse().join("")
            str = stk[stk.length - 1] + str
            stk.pop()
        } else {
            str += ch
        }
    }
    return str
};

console.log(reverseParentheses(s = "a(bcdefghijkl(mno)p)q"))