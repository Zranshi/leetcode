// @Time     : 2021/05/28 17: 47
// @Author   : Ranshi
// @File     : 461. 汉明距离.js
/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
const hammingDistance = function (x, y) {
    let res = 0, bin = x ^ y
    while (bin !== 0) {
        res += bin & 1 === 1
        bin >>= 1
    }
    return res
};


console.log(hammingDistance(x = 93, y = 73))