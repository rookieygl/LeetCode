"""
冒泡排序O(n^2)
冒泡排序的基本思想是，两两比较相邻记录的关键字，如果是反序则交换，直到没有反序为止
"""


class Solution(object):
    def bubbleSort(self, nums):
        length = len(nums)
        for i in range(length):
            for j in range(length - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            print(nums)
        return nums


if __name__ == '__main__':
    # solution = Solution()
    # fun = solution.bubbleSort([6, 9, 3, 7, 15])
    # print(fun)
    l = [0, 1, 2, 3]
    print(l[-1:-2])
