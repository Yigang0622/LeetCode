from typing import List

# 1002. 查找常用字符
# https://leetcode-cn.com/problems/find-common-characters/

class Solution:

    def commonChars(self, A: List[str]) -> List[str]:
        # print(A)
        min_freq = [float('inf')] * 26
        for word in A:
            freq_vector = [0] * 26
            for c in word:
                freq_vector[ord(c) - 97] += 1

            for i in range(26):
                min_freq[i] = min(min_freq[i], freq_vector[i])
        # print(min_freq)
        ans = []
        for i in range(26):
            if min_freq[i] != 0:
                chr_arr = [chr(i+97)] * min_freq[i]
                ans.extend(chr_arr)
        return ans



A = ["bella","label","roller"]
s  = Solution().commonChars(A)
print(s)