"""
"""


class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        n = len(nums)
        ans = []
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
                ans.append(nums[fast])
            fast += 1
        print(ans)
        return slow


if __name__ == '__main__':
    solution = Solution()
    fun = solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(fun)
