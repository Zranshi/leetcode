// @Time     : 2021/05/28 17: 46
// @Author   : Ranshi
// @File     : 1. 两数之和.js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = function(nums, target) {
	let map = new Map();
	for (let i in nums) {
		if (map.has(target - nums[i])) {
			return [map.get(target - nums[i]), i];
		} else {
			map.set(nums[i], i);
		}
	}
};

console.log(twoSum((nums = [2, 7, 11, 15]), (target = 9)));
