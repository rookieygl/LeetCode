"""
有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
"""


class Solution(object):
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        # 利用栈的数据结构，将左括号逆序存储
        stack = list()
        for c in s:
            if c in pairs:
                # 非空很重要 因为会有右括号在前的情况
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        # stack为空，就是有效括号
        return not stack


if __name__ == '__main__':
    solution = Solution()
    fun = solution.isValid("}{")
    print(fun)
