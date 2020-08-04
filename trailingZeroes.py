# 阶乘后的0

def factorial(x):
    if x == 1:
        return x
    else:
        return x*factorial(x-1)

for i in range(1,10):
    print(i, factorial(i))