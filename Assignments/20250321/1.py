"""
写一个程序合并两个字典
"""

dict1 = {}
dict2 = {}

n = int(input("n1: "))
for i in range(n):
    key = input("key: ")
    val = input("val: ")
    dict1[key] = val

n = int(input("n2: "))
for i in range(n):
    key = input("key: ")
    val = input("val: ")
    dict2[key] = val

dict_merged = dict1.copy()
dict_merged.update(dict2)

print(dict_merged)
