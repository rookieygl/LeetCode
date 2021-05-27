"""
汉明距离

两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。也就是记录1的个数
给出两个整数 x 和 y，计算它们之间的汉明距离。
两个等长字符串s1与s2之间的汉明距离定义为将其中一个变为另外一个所需要作的最小替换次数。例如字符串“1111”与“1001”之间的汉明距离为2。
"""


class Solution(object):
    def hammingDistance(self, x, y):
        # 取异或值得到明汉值 0 相同 1 不同 1的个数就是明汉距离
        s = x ^ y
        ret = 0
        while s:
            # 依次位移明汉值 和1取与，1与1的1 就累加
            ret += s & 1
            s >>= 1
        return ret

    # bin 将明汉距离值转成二进制 遍历二进制 等于1的放进list，list长度就是明汉距离
    def hammingDistance_api(self, x, y):
        return len(list(filter(lambda x: x == '1', bin(x ^ y))))


if __name__ == '__main__':
    solution = Solution()
    fun = solution.hammingDistance(1, 4)
    print(fun)
