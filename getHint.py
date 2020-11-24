# 299. 猜数字游戏
# https://leetcode-cn.com/problems/bulls-and-cows/

# 你写出一个秘密数字，并请朋友猜这个数字是多少。
# 朋友每猜测一次，你就会给他一个提示，告诉他的猜测数字中有多少位属于数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位属于数字猜对了但是位置不对（称为“Cows”, 奶牛）。
# 朋友根据提示继续猜，直到猜出秘密数字。

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        pos_dict = dict()
        for i, each in enumerate(secret):
            if each in pos_dict:
                pos_dict[each].add(i)
            else:
                pos_dict[each] = {i}

        count_bull = 0
        count_cows = 0
        count_dict = dict()

        for i, each in enumerate(guess):
            if each in pos_dict:
                if each in count_dict:
                    count_dict[each] += 1
                else:
                    count_dict[each] = 1

                if i in pos_dict[each]:
                    if count_dict[each] <= len(pos_dict[each]):
                        count_bull += 1
                    else:
                        if count_cows >= 1:
                            count_cows -= 1
                            count_bull += 1
                else:
                    if count_dict[each] <= len(pos_dict[each]):
                        count_cows += 1

        return '{}A{}B'.format(count_bull, count_cows)


secret = "1122"
guess  = "1222"
r = Solution().getHint(secret, guess)
print(r)