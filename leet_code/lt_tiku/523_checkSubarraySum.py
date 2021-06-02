"""
连续的子数组和

给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
子数组大小 至少为 2 ，且
子数组元素总和为 k 的倍数。
如果存在，返回 true ；否则，返回 false 。
如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。

前缀和
prefixSums[q]-prefixSums[p]为k的倍数时，余数相等。

公式为:x,y为数组下标
a+b+c=x*k+rem
a+b+c+d=y*k+rem
sum(abcd)-sum(abc) = (y*k+rem)-(x*k+rem)
                   = (y-x)*k

只需要计算每个下标对应的前缀和除以k的余数即可
拓展下 找出所有的连续数组
"""
from itertools import accumulate


class Solution(object):
    # 前缀和求差值
    def checkSubarraySum_difference(selfnums, nums, k):
        length = len(nums)
        if length < 2:
            return False
        sumMap = {0: -1}
        remainder = 0
        for i in range(length):
            remainder = (remainder + nums[i]) % k
            if remainder in sumMap:
                preIndex = sumMap[remainder]
                if i - preIndex >= 2:
                    return True
            else:
                sumMap[remainder] = i
        return False

    # 遍历前缀和
    def checkSubarraySum_sum(selfnums, nums, k):
        length = len(nums)
        if length < 2:
            return False

        total = list(accumulate(nums))
        total.insert(0, 0)
        sumSet = set()
        # length加1，因为total追加了一个元素
        for i in range(2, length + 1):
            sumSet.add(total[i - 2] % k)
            if total[i] % k in sumSet:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    # fun = solution.checkSubarraySum_difference(nums=[2, 4, 3], k=6)
    fun = solution.checkSubarraySum_sum(nums=[6, 0], k=6)
    print(fun)
