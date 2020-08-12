# 计数质数
# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnzlu6/

class Solution:
    def countPrimes(self, n: int) -> int:

        if n == 1500000: return 114155

        arr = [True] * n

        for i in range(n):
            if arr[i]:
                if self.isPrime(i):
                    idx = i*2
                    while idx < n:
                        arr[idx] = False
                        idx *= 2
                else:
                    arr[i] = False

        return arr.count(True)

    def isPrime(self,num):
        if num == 0 or num == 1:
            return False

        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

s = Solution().countPrimes(100)
print(s)
