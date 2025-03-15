"""
写一个程序输出满足下列条件的矩阵:
(1) 矩阵行列由键盘输入
(2) 矩阵元素的值为矩阵行列序号的乘积
"""

m = int(input("m = "))
n = int(input("n = "))

A = []

for i in range(m):
    row = []
    for j in range(n):
        row.append((i + 1) * (j + 1))
    A.append(row)

print(A)
