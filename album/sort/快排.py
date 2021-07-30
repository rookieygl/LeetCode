"""
快速排序O(nlogn)
冒泡排序的基本思想是，两两比较相邻记录的关键字，如果是反序则交换，直到没有反序为止
"""


class Solution(object):
    def sortArray(self, nums):
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, start, end):
        if start >= end:
            return

        pivot = nums[start]
        left, right = start, end
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1

            nums[left] = nums[right]

            while left < right and nums[left] < pivot:
                left += 1
            nums[right] = nums[left]

        nums[left] = pivot
        self.quicksort(nums, start, left - 1)
        self.quicksort(nums, left + 1, end)


if __name__ == '__main__':
    solution = Solution()
    arr = [5, 2, 3, 1]
    solution.sortArray(arr)
    print(arr)
