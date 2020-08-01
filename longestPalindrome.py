# 无重复字符的最长子串
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/79/

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        temp = ''
        for i in range(1, len(s)):

            sub = self.calLongestPalindrome(s, i, i)
            if len(temp) < len(sub):
                temp = sub

            if s[i] == s[i-1]:
                sub = self.calLongestPalindrome(s, i-1, i)
                if len(temp) < len(sub):
                    temp = sub

        return temp


    def calLongestPalindrome(self,s,i,j):

        while i >= 1 and j < len(s) - 1:
            if s[i-1] != s[j+1]:
                return s[i:j+1]
            i -= 1
            j += 1

        return s[i:j+1]


s = 'abbab'
r = Solution().longestPalindrome(s)