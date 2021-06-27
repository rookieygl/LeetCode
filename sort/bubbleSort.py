"""
冒泡排序
冒泡排序的基本思想是，两两比较相邻记录的关键字，如果是反序则交换，直到没有反序为止
"""


class Solution(object):
    def bubbleSort(self, num):
        length = len(num)
        for i in range(length - 1):
            for j in range(i - 1, length - 1):
                if num[j] > num[j + 1]:
                    num[j], num[j + 1] = num[j + 1], num[j]
        return num


if __name__ == '__main__':
    solution = Solution()
    fun = solution.bubbleSort([6, 9, 3, 7, 15])
    print(fun)
