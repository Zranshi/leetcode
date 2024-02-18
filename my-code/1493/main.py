class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        ans = 0
        p0 = p1 = 0
        for num in nums:
            if num == 0:
                p1, p0 = p0, 0
            else:
                p0 += 1
                p1 += 1
            ans = max(ans, p1)
        if ans == len(nums):
            ans -= 1
        return ans


print(Solution().longestSubarray(nums=[1, 1, 0, 1]))
