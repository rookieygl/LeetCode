"""
6.Z字形变换

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows)
"""


class Solution(object):
    def convert(self, s, numRows):
        if numRows <= 1:
            return s
        # 计算多少行
        rows = min(len(s), numRows)  # 算出全部非空行
        rowStrList = list()
        for i in range(rows):
            rowStrList.append([])

        curRow = 0  # curRow大于0小于rows
        goingDown = False
        for index, c in enumerate(s):
            rowStrList[curRow].append(c)
            if curRow == 0 or curRow == numRows - 1:
                goingDown = bool(1 - goingDown)
            curRow += 1 if goingDown else -1

        ans = []
        for i in range(len(rowStrList)):
            ans.append("".join(rowStrList[i]))
        return "".join(ans)


if __name__ == '__main__':
    solution = Solution()
    convert = solution.convert("PAYPALISHIRING", 3)
    print(convert)
