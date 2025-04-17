"""
写一个函数将字符串逆序
"""


def revrs_str(s):
    return s[::-1]


if __name__ == "__main__":
    S = input("str = ")
    revrs_s = revrs_str(S)
    print("Reversed str =", revrs_s)
