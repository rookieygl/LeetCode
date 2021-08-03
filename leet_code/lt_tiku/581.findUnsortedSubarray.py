"""
581. 最短无序连续子数组
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
请你找出符合题意的 最短 子数组，并输出它的长度。
"""


class Solution(object):
    def findUnsortedSubarray_sort(self, nums):
        n = len(nums)

        def is_sorted():
            for i in range(1, n):
                if nums[i - 1] > nums[i]:
                    return False
            return True

        if is_sorted():
            return 0
        nums_sort = sorted(nums)
        left = 0
        while nums[left] == nums_sort[left]:
            left += 1
        right = n - 1
        while nums[right] == nums_sort[right]:
            right -= 1
        return right - left + 1

    def findUnsortedSubarray_loop(self, nums):
        n = len(nums)
        maxn, right = float('-inf'), -1
        minn, left = float('inf'), -1
        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]
        return 0 if right == -1 else right - left - 1


if __name__ == '__main__':
    solution = Solution()
    fun = solution.findUnsortedSubarray_loop([2, 6, 4, 8, 10, 9, 15])
    print(fun)
