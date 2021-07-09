"""
面试题 10.01. 合并排序的数组

给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
初始化 A 和 B 的元素数量分别为 m 和 n。

经典双指针问题
"""


class Solution(object):
    # 双指针
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
