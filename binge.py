# A + A的各位数字的和 = B
# 已知 B，求所有可能的 A。
#
# 例如：
# 123456789 +  （1+2+3+4+5+6+7+8+9） =  123456834
#
# 所以
# Input 123456834
# Output 123456789
# 数字不超过 2^32


n = 2 ** 32 - 1
print(n)

def sum_each_digit(n):
    sum = 0
    while n > 0:
        sum += n%10
        n = n//10
    return sum


start = n - 83
if start < 0:
    start = 0

for i in range(start, n):
    if sum_each_digit(i) + i == n:
        print(i)