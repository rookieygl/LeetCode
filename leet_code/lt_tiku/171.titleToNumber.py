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
        ans, multiple = 0, 1
        for i in range(len(columnTitle) - 1, -1, -1):
            tmp = ord(columnTitle[i]) - ord('A') + 1
            ans += tmp * multiple
            multiple *= 26
        return ans


if __name__ == '__main__':
    solution = Solution()
    fun = solution.titleToNumber("AA")
    print(fun)
