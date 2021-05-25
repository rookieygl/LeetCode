"""
"""


class Solution(object):
    def __init__(self):
        self.INT_MAX = 2 ** 31 - 1
        self.INT_MIN = -2 ** 31
        self.state = "start"
        self.sign = 1
        self.ans = 0
        self.tab = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def GetTabIndex(self, c):
        # 空格
        if c.isspace():
            return 0
        elif c == "+" or c == "-":
            return 1
        elif c.isdigit():
            return 2
        return 3

    # 字符串有限状态自动机
    def AtoiGet(self, c):
        self.state = self.tab[self.state][self.GetTabIndex(c)]
        if self.state == "in_number":
            self.ans = self.ans * 10 + int(c)
        elif self.state == "signed":
            self.sign = 1 if c == '+' else -1

    def myAtoi(self, str):
        for c in str:
            self.AtoiGet(c)
        self.ans = min(self.ans, self.INT_MAX) if self.sign == 1 else min(self.ans, -self.INT_MIN)
        return self.ans * self.sign


if __name__ == '__main__':
    solution = Solution()
    atoi = solution.myAtoi("  a   123")
    print(atoi)
