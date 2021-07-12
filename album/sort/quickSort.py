"""
快速排序O(nlogn)
冒泡排序的基本思想是，两两比较相邻记录的关键字，如果是反序则交换，直到没有反序为止
"""


class Solution(object):
    def sortArray(self, nums):
        self.quicksort(nums, 0, len(nums) - 1)

    def quicksort(self, nums, start, end):
        if start >= end:
            return

        pivot = nums[(start + end) // 2]
        left, right = start - 1, end + 1
        while left < right and nums[right] >= pivot:
            right -= 1

        while left < right and nums[left] < right:
            left += 1

        if left < right:
            nums[left] = nums[right]

        self.quicksort(nums, left, right)
        self.quicksort(nums, right + 1, end)


if __name__ == '__main__':
    solution = Solution()
    arr = [6, 9, 3, 7, 15]
    solution.sortArray(arr)
    print(arr)
