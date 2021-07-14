"""
"""
from random import random


class Solution(object):
    def sortArray(self, nums):
        n = len(nums)

        def QuickSort(left, right):
            if left >= right:
                return nums
            index = random.randint(left, right)
            pivot = nums[index]
            nums[index], nums[left] = nums[left], nums[index]
            i, j = left, right
            while i < j:
                while i < j and nums[j] > pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            QuickSort(left, i - 1)
            QuickSort(i + 1, right)
            return nums

        return QuickSort(0, n - 1)


if __name__ == '__main__':
    solution = Solution()
    fun = solution.sortArray([5, 2, 3, 1])
    print(fun)
