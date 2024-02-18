class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candie = max(candies)
        res = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candie:
                res.append(True)
            else:
                res.append(False)
        return res


print(Solution().kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
