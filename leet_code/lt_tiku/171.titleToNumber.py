"""
171. Excel表列序号
给定一个Excel表格中的列名称，返回其相应的列序号。
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
    def titleToNumber(self, columnTitle):
        number, multiple = 0, 1
        for i in range(len(columnTitle) - 1, -1, -1):
            number += (ord(columnTitle[i]) - ord("A") + 1) * multiple
            multiple *= 26
        return number


if __name__ == '__main__':
    solution = Solution()
    fun = solution.titleToNumber("A")
    print(fun)
