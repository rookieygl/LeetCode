"""
1
"""


class Solution(object):
    def addSortArr(self, A, m, B, n):
        p1, p2 = 0, 0
        addArr = []
        while p1 < m or p2 < n:
            if p1 == m:
                cur = B[p2]
                p2 += 1
            elif p2 == n:
                cur = A[p1]
                p1 += 1
            elif A[p1] <= B[p2]:
                cur = A[p1]
                p1 += 1
            else:
                cur = B[p2]
                p2 += 1
            addArr.append(cur)
        return addArr

    def addArr(self, s):
        self


if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 4]
    B = [0, 2, 100]
    arr = solution.addSortArr(A, len(A), B, len(B))
    print([arr])
