"""
"""


class Solution(object):
    def totalHammingDistance(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans


if __name__ == '__main__':
    solution = Solution()
    fun = solution.totalHammingDistance([4, 14, 2])
    print()
