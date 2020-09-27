
# 279. 完全平方数
# https://leetcode-cn.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:

        if n ** 0.5 == int(n**0.5):
            return 1
        # square_nums = set()
        # i = 1
        # while i <= n ** 0.5:
        #     square_nums.add(i*i)
        #     i += 1
        #
        # if n in square_nums:
        #     return 1
        # print(square_nums)
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, n+1):
            if i ** 0.5 == int(i**0.5):
                dp[i] = 1
            else:
                # for (int j = 1; i - j * j >= 0; j++) {
                j = 1
                while i - j * j >= 0:
                    dp[i] = min(dp[i], dp[i - j * j] + 1)
                    j += 1
                # for j in range(1, i//2 + 1):
                #     print(j, i - j)
                #     dp[i] = min(dp[i], dp[j] + dp[i - j])
        print(dp)
        return dp[-1]

r = Solution().numSquares(12)
print(r)