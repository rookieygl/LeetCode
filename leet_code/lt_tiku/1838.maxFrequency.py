"""
1838. 最高频元素的频数
元素的 频数 是该元素在一个数组中出现的次数。

给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。

执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数。
"""


class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        n = len(nums)
        left = 0
        total = 0
        ans = 1
        for r in range(1, n):
            total += (nums[r] - nums[r - 1]) * (r - left)
            while total > k:
                total -= nums[r] - nums[left]
                left += 1
            ans = max(ans, r - left + 1)
        return ans


if __name__ == '__main__':
    solution = Solution()
    fun = solution.maxFrequency(nums=[1, 2, 4], k=5)
    print(fun)
