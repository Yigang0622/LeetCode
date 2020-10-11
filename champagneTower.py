# LeetCode
# champagneTower 
# Created by Yigang Zhou on 2020/10/10.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 799. 香槟塔
# https://leetcode-cn.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        level = 100
        simulator = [[0.0]*(x+1) for x in range(level)]
        print(simulator)
        simulator[0][0] = poured

        overflowed = False
        if poured > 1:
            overflowed = True

        for i, level in enumerate(simulator):
            # print('Simulating level', i)
            if not overflowed:
                break
            overflowed = False
            for j, glass in enumerate(level):
                if glass > 1:
                    overflowed = True
                    overflow = (glass - 1) / 2
                    if i + 1 < 100: #防止越界
                        simulator[i+1][j] += overflow
                        if j + 1 < 100:
                            simulator[i+1][j+1] += overflow
            if i == query_row:
                break
        # print(simulator)
        ans = simulator[query_row][query_glass]
        print(simulator)

        # 一个杯子最多装1
        if ans > 1:
            return 1
        return ans





s = Solution().champagneTower(1000000000,99,99)
print(s)
