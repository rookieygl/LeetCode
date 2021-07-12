"""
215. 数组中的第K个最大元素

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        # 第k个最大的元素，即升序排列后，index为len(nums)-k
        k = len(nums) - k
        low = 0
        high = len(nums) - 1
        while low <= high:
            p = self.patition(nums, low, high)
            if k < p:
                high = p - 1
            elif k > p:
                low = p + 1
            else:
                return nums[p]
        return -1

    def patition(self, alist, low, high):
        mid_value = alist[low]
        while low < high:
            while low < high and alist[high] >= mid_value:
                high -= 1
            alist[low] = alist[high]

            while low < high and alist[low] <= mid_value:
                low += 1
            alist[high] = alist[low]
        alist[low] = mid_value
        return low


if __name__ == '__main__':
    solution = Solution()
    fun = solution.findKthLargest([3, 2, 1, 5, 6, 4], 5)
    print(fun)
