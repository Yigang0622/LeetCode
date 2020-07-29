from typing import List
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/49/backtracking/92/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.search([],n,n,n, ans)
        return ans

    def search(self, current, open_num, close_num, n, ans):
        if len(current) == 2*n:
            a = ''.join(current)
            ans.append(a)
            return

        if 0 < open_num <= n:
            current.append('(')
            self.search(current, open_num-1, close_num,n, ans)
            current.pop()

        if 0 < close_num <= n and close_num > open_num:
            current.append(')')
            self.search(current, open_num,close_num-1,n, ans)
            current.pop()


r = Solution().generateParenthesis(3)
print(r)