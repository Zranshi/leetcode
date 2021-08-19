// @Time     : 2021/05/28 17: 47
// @Author   : Ranshi
// @File     : 9. 回文数.js

const isPalindrome = function (x) {
  if (x < 0 || (x % 10 == 0 && x != 0)) {
    return false
  }
  let idx = 0
  while (x > idx) {
    idx = idx * 10 + x % 10
    x = Math.floor(x / 10)
  }
  return x === idx || x == Math.floor(idx / 10)
}


console.log(isPalindrome(x = 121))