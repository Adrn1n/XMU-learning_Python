"""
写一个程序从字典中删除某个关键字
"""

dict = {}

n = int(input("n: "))
for i in range(n):
    key = input("key: ")
    val = input("val: ")
    dict[key] = val

key = input("key to del: ")

dict.pop(key, None)

print(dict)
