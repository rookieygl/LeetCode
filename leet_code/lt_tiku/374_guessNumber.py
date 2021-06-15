"""
"""


def guess(num):
    if num > 9:
        return -1
    elif num < 9:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        start, end = 1, n
        while start < end:
            mid = (start + end) // 2
            if guess(mid) <= 0:
                end = mid
            else:
                start = mid + 1
        return start


if __name__ == '__main__':
    solution = Solution()
    fun = solution.guessNumber(100)
    print(fun)
