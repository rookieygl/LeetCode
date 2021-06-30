"""
168. Excel表列名称

给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
"""


class Solution(object):
    def convertToTitle(self, columnNumber):
        ans = list()
        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26
        return "".join(ans[::-1])


if __name__ == '__main__':
    solution = Solution()
    fun = solution.convertToTitle(2)
    print(fun)
