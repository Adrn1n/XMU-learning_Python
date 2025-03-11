"""
写一个程序将列表中的重复元素删除
"""

n = int(input("n: "))
A = []

for i in range(n):
    A.append(int(input()))

uniqueA = list(dict.fromkeys(A))
print("Remove duplicate:", uniqueA)
