// @Time     : 2021/05/28 17: 47
// @Author   : Ranshi
// @File     : 6. Z 字形变换.js
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
const convert = function (s, numRows) {
  if (numRows === 1) {
    return s;
  }
  const len = Math.min(s.length, numRows),
    rows = [];
  for (let i = 0; i < len; i++) {
    rows[i] = '';
  }
  let loc = 0,
    down = false;
  for (const c of s) {
    rows[loc] += c;
    if (loc === 0 || loc === numRows - 1) {
      down = !down;
    }
    loc += down ? 1 : -1;
  }
  let ans = '';
  for (const row of rows) {
    ans += row;
  }
  return ans;
};

console.log(convert((s = 'PAYPALISHIRING'), (numRows = 4)));
