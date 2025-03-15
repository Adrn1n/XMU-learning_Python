"""
写一个程序输出下列图形
*
**
***
****
*****
****
***
**
*
"""

n = int(input("n = "))

for i in range(1, n + 1):
    print("*" * i)
else:
    for i in range(n - 1, 0, -1):
        print("*" * i)
