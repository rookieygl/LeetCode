"""
寻找第K大

有一个整数数组，请你根据快速排序的思路，找出数组中第K大的数。

给定一个整数数组a,同时给定它的大小n和要找的K(1<=K<=n)，请返回第K大的数(包括重复的元素，不用去重)，保证答案存在。

# 第k个最大的元素，即升序排列后，index为len(nums)-k
"""


# 快排思想
# 时间复杂度相比堆排序慢

class Solution:
    def findKth(self, a, n, k):
        k = n - k
        low = 0
        high = n - 1
        while low <= high:
            p = self.patition(a, low, high)
            if k < p:
                high = p - 1
            elif k > p:
                low = p + 1
            else:
                return a[p]
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
    fun = solution.findKth([1, 3, 5, 2, 2], 5, 3)
    print(fun)
