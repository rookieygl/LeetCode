"""
"""


class Solution(object):
    def threeSum(self, nums):
        hashtable = dict()
        targetIndex = []
        # 遍历数组和坐标
        for i, num in enumerate(nums):
            # 当差值存在map时，返回坐标即可
            target = 0 - num
            hashtable[num] = i
            for j, tarNum in enumerate(nums):
                if j == i:
                    continue
                if target - tarNum in hashtable:
                    targetIndex.append([i, hashtable[target - tarNum], j])
                hashtable[tarNum] = j

        # 答案不存在的情况
        return targetIndex


if __name__ == '__main__':
    solution = Solution()
    fun = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(fun)
