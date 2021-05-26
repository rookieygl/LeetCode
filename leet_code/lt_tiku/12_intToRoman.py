"""
整数转罗马数字
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
"""


class Solution(object):
    def __init__(self):
        self.VALUE_SYMBOLS = [
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
        self.THOUSANDS = ["", "M", "MM", "MMM"]
        self.HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        self.TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        self.ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    # 数字模拟 范围有限
    def intToRomanMock(self, num):
        roman = list()
        for value, symbol in self.VALUE_SYMBOLS:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return "".join(roman)

    # 硬编码，范围有限
    def intToRomanCode(self, num):
        return self.THOUSANDS[num // 1000] + self.HUNDREDS[num % 1000 // 100] + self.TENS[num % 100 // 10] + self.ONES[
            num % 10]


if __name__ == '__main__':
    solution = Solution()
    fun = solution.intToRomanMock(6)
    print(fun)
