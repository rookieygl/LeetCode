"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
from random import random


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def fun(self, total, nums):
        redCmap = {}
        for num in range(1, nums):
            redC = random.next(0, total)  # 0,100 12    ->0,88
            redCmap[num] = redC
            total = total - redC
        nums[0] = total


if __name__ == '__main__':
    solution = Solution()
    fun = solution.fun(100, 8)
    print(fun)
