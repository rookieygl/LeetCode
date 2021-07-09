"""
找出旋转数组最小值
数组为升序，旋转一次
"""


class Solution(object):
    def findMin_loop(self, nums):
        ans = numbers[0]
        for num in range(1, len(numbers)):
            ans = min(ans, numbers[num])
        return ans

    #  二分查找
    def findMin_binarySearch(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


if __name__ == '__main__':
    solution = Solution()
    fun = solution.findMin_binarySearch([7, 9, 1, 2, 3, 5])
    print(fun)
