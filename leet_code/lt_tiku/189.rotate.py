"""
189. 旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
"""


class Solution(object):
    # 插入 insert 会将坐标后的元素后移
    def rotate_insert(self, nums, k):
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())

    # 拼接
    def rotate_add(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

    # 三个翻转 整体翻转,前k翻转,后k翻转
    def rotate_reverse(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        print(nums)
        nums[:k] = nums[:k][::-1]
        print(nums)
        nums[k:] = nums[k:][::-1]
        print(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 2]
    solution.rotate_reverse(nums, 2)
