"""
03.找出数组中重复的数字。

找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
"""


class Solution(object):
    def findRepeatNumber(self, nums):
        for index, num in enumerate(nums):
            if index == num:
                continue
            if nums[nums[index]] == nums[index]:
                return nums[index]
            nums[nums[index]], nums[index] = nums[index], nums[nums[index]]
        return -1


if __name__ == '__main__':
    solution = Solution()
    fun = solution.findRepeatNumber([2, 3, 1, 0, 2, 5, 3])

    print(fun)
