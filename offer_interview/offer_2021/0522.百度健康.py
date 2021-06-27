"""
1、合并有序数组
2、找出字符串中的数字
"""


class Solution(object):
    def addSortArr(self, A, m, B, n):
        pa, pb = 0, 0
        addArr = []
        while pa < m or pb < n:
            if pa == m:
                cur = B[pb]
                pb += 1
            elif pb == n:
                cur = A[pa]
                pa += 1
            elif A[pa] <= B[pb]:
                cur = A[pa]
                pa += 1
            else:
                cur = B[pb]
                pb += 1
            addArr.append(cur)
        return addArr

    def findNumberInString(self, s):
        num = ""
        for sub in s:
            if sub.isdigit():
                num += sub
        return int(num)


if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 3, 0, 0, 0]
    B = [2, 5, 6]
    arr = solution.addSortArr(A, 3, B, 3)
    print([arr])

    arr = solution.findNumberInString("1234")
    print(arr)
