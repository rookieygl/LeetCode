"""
面试题 08.08. 有重复字符串的排列组合
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。
"""


class Solution(object):
    def permutation(self, S):
        S = sorted(S)

        def dfs(index):
            if len(path) == len(S):
                res.append("".join(path))
                return
            for i in range(len(S)):
                if S[i] == 0:
                    continue
                if S[i] == S[i - 1] and i > 0:
                    continue
                path.append(S[i])
                S[i] = 0
                dfs(index + 1)
                S[i] = path.pop()

        path = []
        res = []
        dfs(0)
        return res


if __name__ == '__main__':
    solution = Solution()
    fun = solution.permutation("qqe")
    print(fun)
