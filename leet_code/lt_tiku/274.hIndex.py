"""
274. H 指数
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。
且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。

例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    # 计数排序
    def hIndex(self, citations):
        n, total = len(citations), 0
        counter = [0] * (n + 1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1

        for i in range(n, -1, -1):
            total += counter[i]
            if total >= i:
                return i
        return 0

    def hIndex_double_pointer(self, citations):
        left, right = 0, len(citations)

        # 是否
        def can(mid):
            return sum(1 for c in citations if c >= mid)

        while left < right:
            mid = (left + right) // 2
            if mid <= can(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    solution = Solution()
    fun = solution.hIndex_double_pointer([3, 0, 6, 1, 5])
    print(fun)
