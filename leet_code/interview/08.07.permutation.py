"""
面试题 08.07. 无重复字符串的排列组合
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。
"""


class Solution(object):
    def permutation(self, S):
        def dfs(S):
            if S == "":
                ans.append("".join(path))
                return
            for i in range(len(S)):
                path.append(S[i])
                dfs(S[:i] + S[i + 1:])
                path.pop()

        path = []
        ans = []
        dfs(S)
        return ans


if __name__ == '__main__':
    solution = Solution()
    fun = solution.permutation("qwe")
    print(fun)
