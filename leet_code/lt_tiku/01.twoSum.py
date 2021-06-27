"""
两数之和

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。你可以按任意顺序返回答案。
"""


# -*- coding: utf-8 -*-

# 数组元素可重复
class Solution(object):
    def twoSum(self, nums, target):
        hashtable = dict()
        # 遍历数组和坐标
        for i, num in enumerate(nums):
            # 当差值存在map时，返回坐标即可
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        # 答案不存在的情况
        return []


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 4]
    solution_two_sum = solution.twoSum(nums, 6)
    print(solution_two_sum)
