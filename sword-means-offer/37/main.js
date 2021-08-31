// @Time     : 2021/6/30 09:13
// @Author   : Ranshi
// @File     : main.js

function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

const serialize = function (root) {
  return rserialize(root, '');
};

const deserialize = function (data) {
  const dataArray = data.split(',');
  return rdeserialize(dataArray);
};

const rserialize = (root, str) => {
  if (root === null) {
    str += 'None,';
  } else {
    str += root.val + '' + ',';
    str = rserialize(root.left, str);
    str = rserialize(root.right, str);
  }
  return str;
};

const rdeserialize = (dataList) => {
  if (dataList[0] === 'None') {
    dataList.shift();
    return null;
  }

  const root = new TreeNode(parseInt(dataList[0]));
  dataList.shift();
  root.left = rdeserialize(dataList);
  root.right = rdeserialize(dataList);

  return root;
};
