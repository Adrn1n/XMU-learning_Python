"""
写一个类实现 pow(x,n)
"""


class PowCalc:
    """
    一个实现 pow(x, n) 函数的类.

    计算 x 的 n 次幂，支持整数指数 n.
    使用二分幂（快速幂）算法进行高效计算.
    """

    @staticmethod
    def calc(x: float, n: int) -> float:
        """
        计算 x 的 n 次幂 (x^n).

        Args:
            x: 底数 (可以是浮点数或整数).
            n: 指数 (必须是整数).

        Returns:
            x^n 的计算结果 (浮点数).

        Raises:
            ZeroDivisionError: 如果 x 是 0 且 n 是负数.
        """
        if n == 0:
            return 1.0

        res = 1.0
        base = float(x)

        is_negative = False
        if n < 0:
            n = -n
            is_negative = True

        while n > 0:
            if n % 2:
                res *= base

            base *= base
            n //= 2

        if is_negative:
            if not x:
                raise ZeroDivisionError("0 with negative power")
            return 1.0 / res
        else:
            return res


if __name__ == "__main__":
    calculator = PowCalc()

    a = float(input("a = "))
    b = int(input("b (int) = "))

    try:
        result = calculator.calc(a, b)
        print(f"{a}^{b} = {result}")
    except ZeroDivisionError as e:
        print(f"error cal {a}^{b} : {e}")
