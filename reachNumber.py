# 把数列拆成两部分
# P + N = Sum
# P - N = Target
# 两式相减得 Sum - Target = 2N
# 所以Sum - Target 是一个偶数
# 并且 Sum > Target

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        i = 0
        while True:
            # 高速求和公式
            s = ((1 + i) * i) // 2
            if (s - target) % 2 == 0 and s >= target:
                return i
            i += 1

s = Solution().reachNumber(3)
print(s)