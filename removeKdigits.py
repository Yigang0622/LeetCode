# 402. 移掉K位数字
# https://leetcode-cn.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'

        s = []
        for each in num:
            if len(s) == 0:
                s.append(each)
            else:
                if each < s[-1]:
                    while len(s) and k > 0 and each < s[-1]:
                        s.pop()
                        k -= 1
                    s.append(each)
                else:
                    s.append(each)

        return str(int(''.join(s)))


num = "10200"
k = 1
ans = Solution().removeKdigits(num, k)
print(ans)