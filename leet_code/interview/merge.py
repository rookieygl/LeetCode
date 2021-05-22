"""
"""


class Solution(object):
    def merge(self, A, m, B, n):
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
        A[:] = addArr
        return A


if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 4]
    B = [0, 2, 100]
    arr = solution.merge(A, len(A), B, len(B))
    print([arr])
