"""
451. 根据字符出现频率排序
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

Counter
"""
from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        char_freq = []
        counter = Counter(s)
        print(counter.elements())
        for i, j in counter.items():
            char_freq.append([i, j])
        new_li = sorted(char_freq, key=lambda x: -x[1])
        new_char = [i * j for i, j in new_li]
        return ''.join(new_char)


if __name__ == '__main__':
    solution = Solution()
    fun = solution.frequencySort("aaceeee")
    print(fun)
