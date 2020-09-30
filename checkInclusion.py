# 567. 字符串的排列
# https://leetcode-cn.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        vector_1 = self.to_vector(s1)
        vector_2 = [0] * 26
        l = 0
        r = -1
        while r < len(s2) - 1:
            r += 1
            vector_2[ord(s2[r]) - ord('a')] += 1


            while self.contains(vector_1, vector_2) and l < r:
                print(vector_1, vector_2)
                if vector_1 == vector_2:
                    print('DONE')
                    return True

                vector_2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            # 防止左移后上一个while走不到或者一开始就包含的情况, s1= a, s2 = ab 情况
            if vector_1 == vector_2:
                # print('DONE')
                return True

        print("Failed")
        return False

    def to_vector(self, s):
        vector = [0] * 26
        for each in s:
            vector[ord(each) - ord('a')] += 1
        return vector

    def contains(self, vector1, vector2):
        for i, count in enumerate(vector1):
            if count > 0:
                if vector2[i] < count:
                    return False
        return True

s1 = "a"
s2 = "ab"
r = Solution().checkInclusion(s1, s2)
print(r)