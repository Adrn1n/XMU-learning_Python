"""
写一个类将整数转换成罗马数字
"""


class Int2Roman:
    """
    将整数转换成罗马数字

    支持将 1 到 3999 之间的整数转换为罗马数字.
    """

    _Dict = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def convrt(self, integer: int) -> str:
        """
        将给定的整数转换为罗马数字字符串.

        Args:
            integer: 需要转换的整数 (1 <= integer <= 3999).

        Returns:
            对应的罗马数字字符串.

        Raises:
            ValueError: 如果输入不是整数或超出支持的范围 (1-3999).
        """
        if not isinstance(integer, int):
            raise ValueError("input error: not int")
        if not 1 <= integer <= 3999:
            raise ValueError("input error: not in [1, 3999]")

        roman_numeral = ""
        num = integer

        for val, sym in self._Dict:
            while num >= val:
                roman_numeral += sym
                num -= val
            if num == 0:
                break

        return roman_numeral


if __name__ == "__main__":
    converter = Int2Roman()

    num = int(input("num (int in [1,3999]) = "))

    try:
        roman = converter.convrt(num)
        print(f"{num} : {roman}")
    except ValueError as e:
        print(f"error converting {num} : {e}")
