"""
快速排序O(nlogn)
冒泡排序的基本思想是，两两比较相邻记录的关键字，如果是反序则交换，直到没有反序为止
"""


class Solution(object):
    def sortArr(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, low, high):
        if low < high:
            index = self.movePivot(nums, low, high)
            self.quickSort(nums, low, index - 1)
            self.quickSort(nums, index + 1, high)

    def movePivot(self, nums, low, high):
        pivot = nums[low]
        while low < high and nums[high] >= pivot:
            high -= 1
        if low < high:
            nums[low] = nums[high]
        while low < high and nums[low] < pivot:
            low += 1
        if low < high:
            nums[high] = nums[low]

        nums[low] = pivot
        return low


if __name__ == '__main__':
    solution = Solution()
    fun = solution.sortArr([6, 9, 3, 7, 15])
    print(fun)
