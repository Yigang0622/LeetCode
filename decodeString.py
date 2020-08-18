# 字符串解码
# https://leetcode-cn.com/leetbook/read/queue-stack/gdwjv/

class Solution:
    def decodeString(self, s: str) -> str:
        print(s)
        stack = []
        buffer = ''
        for each in s:
            if each == '[':
                if buffer != '':
                    stack.append(buffer)
                buffer = ''
                stack.append('[')
            elif each == ']':
                if buffer != '':
                    stack.append(buffer)
                buffer = ''
                temp = ''
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                stack.append(int(stack.pop()) * temp)
            else:
                if each.isdigit() and buffer.isdigit():
                    buffer += each
                elif each.isdigit() and not buffer.isdigit():
                    if buffer != '':
                        stack.append(buffer)
                    buffer = ''
                    buffer += each
                else:
                    buffer += each

        if buffer != '':
            stack.append(buffer)

        result = ''.join(stack)
        return result


case = "3[a2[c]]"
s = Solution().decodeString(case)
print(s)
