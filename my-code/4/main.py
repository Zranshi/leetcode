# -*- coding: utf-8 - *-
# @Time     : 2021/05/28 17: 48
# @Author   : Ranshi
# @File     : 4. 寻找两个正序数组的中位数.py
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        L = len(nums1) + len(nums2)
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1  # 保持nums1比较长
        if L == 2:
            if len(nums2) == 0:
                return (nums1[0] + nums1[1]) / 2.0
            return (nums1[0] + nums2[0]) / 2.0

        if L % 2 == 0:  # even
            EorO = True
            k = L // 2
        else:  # Odd
            EorO = False
            k = L // 2 + 1

        def helper(s1, s2, k):  # 本质上是找第k小的数
            if len(s1) < len(s2) or (len(s1) == len(s2) and s1[0] > s2[0]):
                s1, s2 = s2, s1  # 保持nums1比较长；或者两个序列长度相等时，保持nums1[0]值最小
            if len(s2) == 0:
                if EorO:
                    # 二序列长度之和为偶数，取nums1的第k小和k-1小数
                    return (s1[k - 1] + s1[k]) / 2.0
                else:
                    return s1[k - 1]  # 二序列长度之和为奇数，直接返回nums1的第k小数
            if k == 1:
                if not EorO:
                    return min(s1[0], s2[0])  # 找最小数，比较数组首位
                n1 = min(s1[0], s2[0])  # 取出最小的首元素
                if n1 == s1[0]:  # 如果第一个序列的首元素最小
                    # 因为此时，二序列长度不为0，nums1至少有两个元素，nums2至少有1个元素
                    return (n1 + min(s1[1], s2[0])) / 2.0
                # 若nums2长度大于1，则取nums2[1]与nums1[0]的较小者与nums2[0]为所需结果
                if len(s2) > 1:
                    return (n1 + min(s1[0], s2[1])) / 2.0
                else:  # 若nums2长度为1，则取nums1[0]与nums2[0]为结果
                    return (n1 + s1[0]) / 2.0
            t = min(k // 2, len(s2))  # 保证不上溢
            # 递归调用，即每次以新的k值和新的nums1（比较后的长序列）nums2（剔掉k/2个元素的新序列）作为递归调用参数
            if s1[t - 1] >= s2[t - 1]:
                return helper(s1, s2[t:], k - t)
            else:
                return helper(s1[t:], s2, k - t)

        return helper(nums1, nums2, k)


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
