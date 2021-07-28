"""
"""


class Solution(object):
    def fun(self):
        return 0


if __name__ == '__main__':
    # nums = [1, 2, 3]
    # res = [nums]
    # res[0][0] = 'banana'
    # print(nums)
    # print(res)
    # nums.append(4)
    # print(nums)
    # print(res)
    #
    # nums1 = [1, 2, 3]
    # res1 = [nums1[:]]
    # res1[0][0] = 'banana'
    # print(nums1)
    # print(res1)
    # nums1.append(4)
    # print(nums1)
    # print(res1)
    nums = [1, 2, 3]
    arr = nums
    nums.append(4)
    print(arr)

    nums = [1, 2, 3]
    arr1 = [0]
    arr1[:] = nums
    nums.append(4)
    print(arr1)
