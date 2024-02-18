class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        res = 0
        counter: dict[int, int] = dict()
        for v in nums:
            if k - v in counter and counter[k - v] > 0:
                res += 1
                counter[k - v] -= 1
            else:
                counter[v] = counter[v] + 1 if v in counter else 1
        return res


print(Solution().maxOperations(nums=[1, 2, 3, 4], k=5))
