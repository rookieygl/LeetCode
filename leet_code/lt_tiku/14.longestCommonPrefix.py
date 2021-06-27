"""
最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。


any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。

在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False

"""


class Solution(object):
    # 横向查找 时间复杂度 O(mn) 空间复杂度 O(1)
    def longestCommonPrefix_horizontal(self, strs):
        if not strs:
            return ""

        def commonPrefix(str1, str2):
            min_len, index = min(len(str1), len(str2)), 0
            while index < min_len and str1[index] == str2[index]:
                index += 1
            return str1[:index]

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = commonPrefix(prefix, strs[i])
            if not prefix:
                break
        return prefix

    # 竖向查找 时间复杂度 O(mn) 空间复杂度 O(1)
    def longestCommonPrefix_vertical(self, strs):
        if not strs:
            return ""
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
        return strs[0]

    '''
    分治
    时间复杂度：O(mn)，其中 mm 是字符串数组中的字符串的平均长度，nn 是字符串的数量。时间复杂度的递推式是 T(n)=2*T(n/2)+O(m)，通过计算可得 T(n)=O(mn)。
    空间复杂度：O(mlog n)O(mlogn)，其中 mm 是字符串数组中的字符串的平均长度，nn 是字符串的数量。空间复杂度主要取决于递归调用的层数，层数最大为 log n，每层需要 mm 的空间存储返回结果。
    '''

    def longestCommonPrefix_divide(self, strs):
        def lcp(start, end):
            # 弹出的必要条件
            if start == end:
                return strs[start]

            mid = start + end // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            # i 从零自增
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]
            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) - 1)

    # 二分查找
    def longestCommonPrefix_dichotomy(self, strs):
        def isCommonPrefix(length):
            # 取出length长度的前缀,遍历字符串数组 都相等返回true
            str_pre, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str_pre for i in range(1, count))

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1
        return strs[0][:low]


if __name__ == '__main__':
    solution = Solution()
    fun = solution.longestCommonPrefix_dichotomy(["dog", "docecar", "dar", "dow"])
    print(any((True, False, False, False)))
    # print(fun)
