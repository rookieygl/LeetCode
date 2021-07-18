"""
面试题 10.02. 变位词组
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。
"""
import collections


class Solution(object):
    def groupAnagrams(self, strs):
        mp = collections.defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        return list(mp.values())


if __name__ == '__main__':
    solution = Solution()
    fun = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(fun)
