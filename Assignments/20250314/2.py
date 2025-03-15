"""
写一个程序输出元组中偶数和奇数的个数
"""

n = int(input("n = "))
A = []

for i in range(n):
    A.append(int(input()))

T = tuple(A)

oddN, evnN = 0, 0

for num in T:
    if num % 2:
        oddN += 1
    else:
        evnN += 1

print("Odd count:", oddN)
print("Even count:", evnN)
