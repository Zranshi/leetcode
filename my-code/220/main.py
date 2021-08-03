# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 03
# @Author   : Ranshi
# @File     : 220. 存在重复元素 III.py
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(
            self,
            nums: List[int],
            k: int, t: int) -> bool:
        from sortedcontainers import SortedSet
        st = SortedSet()
        length, left = len(nums), 0

        for right in range(length):

            if right - left > k:
                st.remove(nums[left])
                left += 1

            index = st.bisect_left(nums[right] - t)

            if st and 0 <= index < len(st) and abs(
                    st[index] - nums[right]) <= t:
                return True

            st.add(nums[right])

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))
