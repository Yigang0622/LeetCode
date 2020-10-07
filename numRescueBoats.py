from typing import List

# 881. 救生艇
# https://leetcode-cn.com/problems/boats-to-save-people/

# 如果最重的人可以与最轻的人共用一艘船，那么就这样安排。否则，最重的人无法与任何人配对，那么他们将自己独自乘一艘船。
# limit 7 -> 5 2 1三个人的话也是优先选择 5和1，因为2都能和最重的5配一条穿了，那么他必然能和剩下的其他人撘乘一条船

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        num = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                # print(people[i], people[j])
                j -= 1
            # else:
            #     print(people[i])
            num += 1
            i += 1
        return num


people =[3,2,2,1]
limit = 3
r = Solution().numRescueBoats(people, limit)
print(r)