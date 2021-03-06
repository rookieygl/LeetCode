# 两数之和
class Solution(object):
    def twoSum(self, nums, target):
        hashtable = dict()
        # 遍历数组和坐标
        for i, num in enumerate(nums):
            # 当差值存在map时，返回坐标即可
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        # 答案不存在的情况
        return []

    # 双指针 寻找每个字符和右侧字符的最长不重复子串
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        charSet = set()  # 记录重复字符
        rk, ans = -1, 0
        for i in range(length):
            if i != 0:
                charSet.remove(s[i - 1])  # 从坐标1开始，每次移除上一个字符
            while rk + 1 < length and s[rk + 1] not in charSet:
                charSet.add(s[rk + 1])  # 移动左指针，从起点开始寻找最大子串
                rk += 1
            # 循环结束，存入最大子串
            ans = max(ans, rk - i + 1)
        return ans


if __name__ == '__main__':
    solution = Solution()
    fun = solution.lengthOfLongestSubstring()
    print(fun)
