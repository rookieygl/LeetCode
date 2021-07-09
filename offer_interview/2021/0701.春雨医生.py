"""
1、输出螺旋矩阵（二维数组）
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 1、查找第k大元素
    def findEle(self, nums):
        return 0

    def quickSort(self, nums):
        self.quick(nums, 0, len(nums))

    def quick(self, nums, left, right):
        while left < right:
            mid = self.partion(nums, left, right)
            self.quick(nums, left, mid - 1)
            self.quick(nums, mid - 1, right)

    def partion(self, nums, left, right):
        
        return 0


if __name__ == '__main__':
    solution = Solution()
    fun = solution.findEle(1)
    arr = [10, 7, 8, 9, 1, 5]
    print(fun)
