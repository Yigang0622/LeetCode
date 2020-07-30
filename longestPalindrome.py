# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/79/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        print(s)
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                sub = self.calLongestPalindrome(s, i-1, i)
                print(sub)
            else:
                sub = self.calLongestPalindrome(s, i, i)
                print('x',sub)


    def calLongestPalindrome(self,s,i,j):

        while i > 1 and j < len(s) - 1:
            i -= 1
            j += 1
            if s[i] != s[j]:
                return s[i-1:j]

        return s[i-1:j]


s = 'bcabacd'
r = Solution().longestPalindrome(s)