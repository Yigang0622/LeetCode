# 实现pow(x,y)

class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0:
            return 0

        if n == 0:
            if x < 0:
                return -1
            elif x > 0:
                return 1
            else:
                return 0

        result = self.pow(x, abs(n))
        if n < 0:
            return 1/result
        else:
            return result

    def pow(self,x ,n):
        if n == 1:
            return x
        else:
            if n % 2 == 0:
                return self.pow(x*x, n/2)
            else:
                return x*self.pow(x*x, (n - 1) / 2)


r = Solution().myPow(-2, -7)
print(r)


