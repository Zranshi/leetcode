# -*- coding: UTF-8 -*-
# @Time     : 2022/07/29 10:21
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 593. 有效的正方形
class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        if p1 == p2 == p3 == p4:
            return False
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4], key=lambda x: x[0] * 10000 + x[1])

        def two_point_distance_pow_2(x, y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

        def vector_multiplication(a, b):
            return a[0] * b[0] + a[1] * b[1]

        return (
            (
                two_point_distance_pow_2(p1, p2)
                == two_point_distance_pow_2(p1, p3)
                == two_point_distance_pow_2(p3, p4)
                == two_point_distance_pow_2(p2, p4)
            )
            and vector_multiplication(
                [p1[0] - p2[0], p1[1] - p2[1]], [p1[0] - p3[0], p1[1] - p3[1]]
            )
            == 0
            and vector_multiplication(
                [p2[0] - p4[0], p2[1] - p4[1]], [p3[0] - p4[0], p3[1] - p4[1]]
            )
            == 0
        )


if __name__ == "__main__":
    print(Solution().validSquare(p1=[0, 0], p2=[0, 0], p3=[0, 0], p4=[0, 0]))
