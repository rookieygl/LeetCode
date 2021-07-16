"""
面试题 17.10. 主要元素
数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。
"""
from collections import Counter


class Solution(object):
    # Counter
    def majorityElement(self, nums):
        major = len(nums) // 2 + 1
        counter = Counter(nums)
        common = counter.most_common(1)
        if common[0][1] >= major:
            return common[0][0]
        return -1

    # set
    def majorityElement_set(self, nums):
        nSet = set(nums)  # 元素去重
        for i in nSet:
            if nums.count(i) > len(nums) / 2:
                return i
        return -1

    # sort
    def majorityElement_sort(self, nums):
        nums.sort()
        tmp, num, maxL = 0, nums[-1], len(nums) // 2
        while nums:
            if nums[-1] == num:
                tmp += 1
                nums.pop()  # 默认-1
            elif tmp > maxL:
                return num
            else:
                tmp = 0
                num = nums[-1]
        return num if tmp > maxL else -1

    # 摩尔投票 vote 投票 主要元素必然剩下
    def majorityElement_vote(self, nums):
        vote, count = 0, 0
        for num in nums:
            if not count:
                vote = num
            if vote == num:
                count += 1
            else:
                count -= 1
        return vote if count and nums.count(vote) > len(nums) // 2 else -1


if __name__ == '__main__':
    solution = Solution()
    fun = solution.majorityElement_vote([1, 3, 1])
    print(fun)
