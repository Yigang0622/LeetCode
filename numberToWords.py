# LeetCode
# numberToWords 
# Created by Yigang Zhou on 2020/10/10.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 273. 整数转换英文表示
# https://leetcode-cn.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        ans = ""
        temp = num % 1000
        ans = ans + self.below_thousand(temp)
        # 防止 1000000 成为 One Billion Zero
        if num // 1000 > 0 and temp == 0:
            ans = ''

        for each in ['Thousand', 'Million', 'Billion']:
            num = num // 1000
            if num > 0:
                temp = num % 1000
                if temp != 0:
                    ans = "{} {} {}".format(self.below_thousand(temp), each, ans).strip()
            else:
                return ans
        return ans

    def below_ten(self, num) -> str:
        arr = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        return arr[num]

    def below_twenty(self, num):
        if num < 10:
            return self.below_ten(num)
        if num == 20:
            return 'Twenty'
        arr = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
               'Nineteen']
        return arr[num % 10]

    def below_hundred(self, num):
        if num <= 20:
            return self.below_twenty(num)
        else:
            ten_digit = num // 10
            digit = num % 10
            arr = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
            if digit == 0:
                return arr[ten_digit]
            else:
                return '{} {}'.format(arr[ten_digit], self.below_ten(digit))

    def below_thousand(self, num):
        if num < 100:
            return self.below_hundred(num)
        hundred_digit = num // 100
        digit = num % 100
        if digit == 0:
            return "{} Hundred".format(self.below_ten(hundred_digit))
        else:
            return "{} Hundred {}".format(self.below_ten(hundred_digit), self.below_hundred(digit))


nums = [1000000,1,0,123456789,123456789123,100010]
for num in nums:
    print(num)
    s = Solution().numberToWords(num)
    print(s)
    print()
