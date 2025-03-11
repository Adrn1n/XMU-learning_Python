"""
写一个程序输出列表中第二大的元素
"""

n = int(input("n: "))
A = []

for i in range(n):
    A.append(int(input()))

max_a = max(A)
B = A[:]

while max_a in B:
    B.remove(max_a)

max2_a = max(B)
print("Second max:", max2_a)
