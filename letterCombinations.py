from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        target_len = len(digits)
        ans = []
        if target_len == 0:
            return []
        self.search([],digits,target_len, ans)
        return ans

    def search(self, current, digits, target_len, ans):
        current_len = len(current)
        if current_len == target_len:
            # print(''.join(current))
            ans.append(''.join(current))
            return
        letters = self.lettersForDigit(digits[current_len])
        for each in letters:
            a = current[:]
            a.append(each)
            self.search(a, digits, target_len, ans)

    def lettersForDigit(self, letter):
        if letter == '2':
            return ['a','b','c']
        elif letter == '3':
            return ['d','e','f']
        elif letter == '4':
            return ['g','h','i']
        elif letter == '5':
            return ['j','k','l']
        elif letter == '6':
            return ['m','n','o']
        elif letter == '7':
            return ['p','q','r','s']
        elif letter == '8':
            return ['t','u','v']
        elif letter == '9':
            return ['w','x','y','z']


r = Solution().letterCombinations('8')
print(r)

