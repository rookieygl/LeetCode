"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""


class Solution(object):
    # 双指针 寻找每个字符和右侧字符的最长不重复子串
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        charSet = set()
        rightKey, ans = -1, 0
        for i in range(n):
            if i != 0:
                charSet.remove(s[i - 1])
            while rightKey + 1 < n and s[rightKey + 1] not in charSet:
                charSet.add(s[rightKey + 1])
                rightKey += 1
            ans = max(ans, rightKey - i + 1)
        return ans


if __name__ == '__main__':
    solution = Solution()
    substring = solution.lengthOfLongestSubstring("abcabcbb")
    print(substring)
