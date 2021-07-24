"""
704. 二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

标准二分，不能再错！！！
"""


class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1  # 右边界不能越界
        while left <= right:
            mid = (left + right) // 2  # pivot = left + (right - left) // 2 这样写可以防止溢出，但是Python不会溢出
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1  # 整除会有损失，需要补偿
        return -1


if __name__ == '__main__':
    solution = Solution()
    fun = solution.search([-1, 0, 3, 5, 9, 12], 2)
    print(fun)
