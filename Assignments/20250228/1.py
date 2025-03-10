"""
写一个程序删除一个非空字符串的第n个字符
"""

S = input("Text\n")
n = int(input("n\n"))
S1 = S[: n - 1] + S[n:]
print(S1)
