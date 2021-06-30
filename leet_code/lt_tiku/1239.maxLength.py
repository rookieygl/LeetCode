"""
1239.串联字符串的最大长度

给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
请返回所有可行解 s 中最长长度。
"""


class Solution(object):
    def maxLength(self, arr):
        ans = 0
        masks = [0]
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord("a")  # ord 返回对应的 ASCII/Unicode 数值
                if (mask >> idx) & 1:  # // 若 mask 已有 ch，则说明 s 含有重复字母，无法构成可行解
                    mask = 0
                    break
                mask |= 1 << idx  # 将 ch 加入 mask 中
            if mask == 0:
                continue
            n = len(masks)
            for i in range(n):
                m = masks[i]
                if (m & mask) == 0:
                    masks.append(m | mask)
                    ans = max(ans, bin((m | mask)).count("1"))
        return ans


if __name__ == '__main__':
    solution = Solution()
    fun = solution.maxLength(["aba", "iq", "ue"])
    print(fun)

    print()
