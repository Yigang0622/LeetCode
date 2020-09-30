# 76. 最小覆盖子串
# https://leetcode-cn.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        l = 0
        r = -1
        t_vec = self.to_vector(t)
        s_vec = dict()
        # if s[0] in t_vec:
        #     s_vec[s[0]] = 1
        min_len = len(s)
        ans = ''
        while r < len(s) - 1:
            r += 1
            if s[r] in t_vec:
                if s[r] in s_vec:
                    s_vec[s[r]] += 1
                else:
                    s_vec[s[r]] = 1


            while self.check_equal(t_vec, s_vec):
                # print(t_vec, s_vec)
                # print(l, r)
                if r - l < min_len:
                    min_len = r - l + 1
                    ans = s[l:r+1]

                if s[l] in s_vec:
                    s_vec[s[l]] -= 1
                    if s_vec[s[l]] == 0:
                        del s_vec[s[l]]
                l += 1

        return ans

    def check_equal(self, t_vec, s_vec):
        for each in t_vec:
            if each not in s_vec:
                return False
            if t_vec[each] > s_vec[each]:
                return False
        return True

    def to_vector(self, t):
        vec = dict()
        for each in t:
            if each not in vec:
                vec[each] = 1
            else:
                vec[each] += 1
        return vec

S = 'ADOBECODEBANC'
T = 'ABC'
s = Solution().minWindow(S, T)
print('Ouput', s)