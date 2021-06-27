"""
连续数组
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

示例 1:
输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
"""


class Solution(object):
    # 击败97%
    def findMaxLength_me(self, nums):
        maxLength, count = 0, 0
        countMap = {0: -1}
        for index, num in enumerate(nums):
            count += -1 if num == 0 else 1
            if count in countMap:
                maxLength = max(maxLength, index - countMap[count])
            else:
                countMap[count] = index
        return maxLength


if __name__ == '__main__':
    solution = Solution()
    fun = solution.findMaxLength_me([0, 1, 0, 1])
    print(fun)
