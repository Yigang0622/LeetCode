# 把数字翻译成字符串
# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/

class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        ans = []
        self.search([],0,s,ans)
        print(ans)
        return len(ans)


    def search(self, current, start, s, ans):
        if start == len(s):
            ans.append(current[:])
            return

        for i in [1, 2]:
            if start+i <= len(s):
                digit = int(s[start:start+i])
                if digit <= 25:
                    if len(s[start:start+i]) == 2 and s[start:start+i][0] == '0':
                        continue
                    current.append(digit)
                    self.search(current,start+i,s,ans)
                    current.pop()




num = 506
r = Solution().translateNum(num)
print(r)