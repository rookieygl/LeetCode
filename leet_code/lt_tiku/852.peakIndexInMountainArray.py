"""
852.山脉数组的峰顶索引

符合下列属性的数组 arr 称为 山脉数组 ：
arr.length >= 3
存在 i（0 < i < arr.length - 1）使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
给你由整数组成的山脉数组 arr ，返回任何满足
arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。

二分，逼近极值
1、二分边界两个条件
    arr[mid] > arr[mid + 1] 向右逼近
    arr[mid] > arr[mid - 1] 向左逼近
2、很多人在问为啥有mid + 1，因为
    mid = (start + end) // 2
这一步可能是奇数，导致向下mid小

三分


枚举
遍历，单调函数，出现
    arr[mid] > arr[mid + 1]
mid就是解


"""


class Solution(object):
    # 官方的二分
    def peakIndexInMountainArray_double(self, arr):
        start, end = 0, len(arr) - 2  # 最后一位必然不是山脉数
        while start < end:
            mid = (start + end) // 2
            if arr[mid] > arr[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start

    # 三分法
    def peakIndexInMountainArray_three(self, arr):
        start, end = 0, len(arr) - 2  # 最后一位必然不是山脉数
        while start < end:
            m1 = start + int((end - start) / 3)
            m2 = end - int((end - start) / 3)
            if arr[m1] > arr[m2]:
                end = m2 - 1
            else:
                start = m1 + 1
        return start


if __name__ == '__main__':
    solution = Solution()
    fun = solution.peakIndexInMountainArray_three([0, 2, 1, 0])
    print(fun)
