"""
找出数组最小值
"""


class Solution(object):
    def findMin_loop(self, n):
        ans = n[0]
        for num in range(1, len(n)):
            ans = min(ans, n[num])
        return ans

    def findMin_binarySearch(self, n):
        s, e = 0, len(n) - 1

        while s < e:
            mid = (s + e) // 2
            if n[mid] > n[s]:
                s = mid + 1
            else:
                e = mid
        return n[s] if n[s] < n[e] else n[e]


if __name__ == '__main__':
    solution = Solution()
    fun = solution.findMin_binarySearch([7, 9, 1, 2, 3, 5])
    print(fun)
