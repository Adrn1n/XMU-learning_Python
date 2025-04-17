"""
写一个函数统计字符串中大写字母和小写字母的个数
"""


def cnt_letter_str(s):
    up = sum(1 for c in s if c.isupper())
    low = sum(1 for c in s if c.islower())
    return up, low


if __name__ == "__main__":
    S = input("str = ")
    upCnt, lowCnt = cnt_letter_str(S)
    print(f"Upper: {upCnt}, lower: {lowCnt}")
