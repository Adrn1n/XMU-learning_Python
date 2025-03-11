"""
写一个程序计算列表中所有元素的和
"""

n = int(input("n: "))
A = []

for i in range(n):
    A.append(int(input()))

total = sum(A)
print("Sum:", total)
