from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        answers = []
        # if self.isPalindromic(s):
        #     answers.append([s])
        self.trace_back(0, s, [], answers)
        return answers

    def trace_back(self, start, s, path, answers):
        if start == len(s):
            answers.append(path[:])
            return

        for i in range(start, len(s)+1):
            sub_str = s[start:i+1]

            if self.isPalindromic(sub_str):
                path.append(sub_str)
                self.trace_back(i + 1, s, path, answers)
                path.pop()

    def isPalindromic(self, str):
        length = len(str)
        for i in range(int(length/2)):
            if str[i] != str[length - i - 1]:
                return False
        return True

r = Solution().partition('efe')
print(r)