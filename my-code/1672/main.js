// @Time     : 2021/12/12 21:17
// @Author   : Ranshi
// @File     : main.js
// @Doc      : 1672. 最富有客户的资产总量
/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function (accounts) {
  let maxSum = 0;
  for (let i = 0; i < accounts.length; i++) {
    let sum = 0;
    for (let j = 0; j < accounts[0].length; j++) {
      sum += accounts[i][j];
    }
    maxSum = Math.max(maxSum, sum);
  }
  return maxSum;
};

console.log(
  maximumWealth(
    (accounts = [
      [1, 2, 3],
      [3, 2, 1],
    ])
  )
);
