"""
面试题 10.03. 搜索旋转数组
搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，
假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。

有重复元素
"""


class Solution(object):
    # 二分查找
    def search(self, arr, target):
        n = len(arr) - 1
        left, right = 0, n
        while left <= right:
            if arr[left] == target:  # 当left符合时直接返回, 因为找的是最小的索引
                return left
            mid = (left + right) // 2
            if arr[mid] == target:  # 只要最小坐标，当中间值等于目标值，将右边界移到中间，因为左边可能还有相等的值
                right = mid
            elif arr[0] < arr[mid]:
                if arr[0] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[0] > arr[mid]:
                if arr[mid] < target <= arr[n]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:  # 当中间数字与左边数字相等时，将左边界右移 最坏复杂度O(n)
                left += 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    arr = solution.search([7, 8, 9, 1, 2], 9)
    print([arr])
