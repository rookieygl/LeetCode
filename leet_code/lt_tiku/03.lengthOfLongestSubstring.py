"""
3.无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""


class Solution(object):
    # 双指针 寻找每个字符和右侧字符的最长不重复子串
    def lengthOfLongestSubstring_doublePonit(self, s):
        length = len(s)
        charSet = set()  # 记录重复字符
        rk, ans = -1, 0
        for i in range(length):
            if i != 0:
                charSet.remove(s[i - 1])  # 从坐标1开始，每次移除上一个字符
            while rk + 1 < length and s[rk + 1] not in charSet:  # rk + 1 < length 防止角标越界
                charSet.add(s[rk + 1])  # 移动左指针，从起点开始寻找最大子串
                rk += 1
            # 循环结束，存入最大子串
            ans = max(ans, rk - i + 1)
        return ans


if __name__ == '__main__':
    solution = Solution()
    substring = solution.lengthOfLongestSubstring_doublePonit("abca")
    print(substring)
