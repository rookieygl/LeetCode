"""
04.二维数组中的查找

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


class Solution(object):
    # 利用数组的递增顺序
    def findNumberIn2DArray(self, matrix, target):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        rows, columns = len(matrix), len(matrix[0])
        row, column = 0, len(matrix[0]) - 1
        while row < rows and column >= 0:
            num = matrix[row][column]
            if num == target:
                return True
            if num > target:
                column -= 1
            if num < target:
                row += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    fun = solution.findNumberIn2DArray(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19],
         [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 31]],
        30)
    print(fun)
