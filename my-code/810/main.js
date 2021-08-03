// @Time     : 2021/05/28 17: 47
// @Author   : Ranshi
// @File     : 810. 黑板异或游戏.js
/**
 * @param {number[]} nums
 * @return {boolean}
 */
const xorGame = function (nums) {
    if (nums.length % 2 === 0) {
        return true
    }
    let xor = 0
    for (const count of nums) {
        xor ^= count
    }
    return xor === 0
};

console.log(xorGame(nums = [1, 1, 2]))