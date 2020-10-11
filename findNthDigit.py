# LeetCode
# findNthDigit 
# Created by Yigang Zhou on 2020/10/10.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 剑指 Offer 44. 数字序列中某一位的数字
# https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/

class Solution:
    def findNthDigit(self, n: int) -> int:

        if n <= 9:
            return n

        number_of_digit = 1
        num = 0
        levels = []
        while num <= n:
            if number_of_digit == 1:
                num += 10
                levels.append(10)
            else:
                total = number_of_digit * (9 * 10**(number_of_digit - 1))
                num += total
                levels.append(total)
            number_of_digit += 1
        print(levels)
        answer_digit_num = number_of_digit-1
        residual = n - sum(levels[:-1])
        start = 10 ** (answer_digit_num-1)
        offset = residual // answer_digit_num
        target_number = start + offset
        # print(target_number)
        pos = residual % answer_digit_num
        # print('pos', pos)
        ans = int(str(target_number)[pos])
        return ans


s = Solution().findNthDigit(1000)
print(s)
