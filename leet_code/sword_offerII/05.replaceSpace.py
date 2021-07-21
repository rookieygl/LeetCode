"""
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
"""


class Solution(object):
    # 单个替换
    def replaceSpace_for(self, s):
        tep = "%20"
        ns = [] * (3 * len(s))
        for c in s:
            if c.isspace():
                ns.append(tep)
            else:
                ns.append(c)
        return "".join(ns)

    # 系统函数速度最快
    def replaceSpace_fun(self, s):
        return s.replace(" ", "%20")


if __name__ == '__main__':
    solution = Solution()
    fun = solution.replaceSpace_for("We are happy.")
    print(fun)
