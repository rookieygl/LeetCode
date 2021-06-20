"""
括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""
from functools import lru_cache


class Solution(object):
    @lru_cache(None)
    def generateParenthesis(self, n):
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans


if __name__ == '__main__':
    solution = Solution()
    fun = solution.generateParenthesis(3)
    print(fun)
