"""
"""


class Solution(object):
    def fun(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
        return nums


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 2]
    fun = solution.fun(nums, 2)
    print(fun)


