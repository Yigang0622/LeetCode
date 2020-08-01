from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        vector_dict = []

        for i,each in enumerate(strs):
            v = self.word_to_vector(each)
            if v in vector_dict:
                idx = vector_dict.index(v)
                ans[idx].append(each)
            else:
                ans.append([each])
                vector_dict.append(v)
        return ans


    def word_to_vector(self, word):
        vector = [0] * 26
        for each in word:
            vector[ord(each) - 97] += 1
        return vector


input = ["eat", "tea", "tan", "ate", "nat", "bat"]
r = Solution().groupAnagrams(input)