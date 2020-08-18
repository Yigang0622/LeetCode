# T9键盘
# https://leetcode-cn.com/problems/t9-lcci/
from typing import List


class Solution:

    charForNum = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],

    }

    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        dictionary = set(words)
        ans = []
        self.search('', num, ans, dictionary)
        return ans

    def search(self, current, num, ans, dictionary):
        if len(num) == 0:
            if current in dictionary:
                ans.append(current)
            return

        for each in self.charForNum[num[0]]:
            word = current + each
            self.search(word, num[1:], ans, dictionary)


r = Solution().getValidT9Words('2', ["a", "b", "c", "d"])
print(r)
