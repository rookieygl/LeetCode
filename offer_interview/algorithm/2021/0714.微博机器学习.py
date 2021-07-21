"""
等式组合
求出a3+b3 = c3+d3所有组合
abcd取值范围1-1000
"""
import collections
import math


class Solution(object):
    def combination(self):
        pow_map = collections.defaultdict(list)
        pow_repeat = collections.defaultdict(str)
        for a in range(1, 10):
            for b in range(1, 10):
                pow_sum = math.pow(a, 3) + math.pow(b, 3)
                comb = "%d+%d" % (a, b)
                comb = str(comb)
                if comb in pow_repeat:
                    continue
                pow_repeat[comb] = True
                pow_map[pow_sum].append(comb)

        def dfs(comb_list, result_list):
            print(str(key) + ":" + str(comb_list))
            if len(comb_list) == 0:
                result_list.append("=".join(path))
                return
            for i in range(len(comb_list)):
                path.append(comb_list[i])
                dfs(comb_list[:i] + comb_list[i + 1:], result_list)
                path.pop()
            return result_list

        for key, value_list in pow_map.items():
            path = []
            result_list = []
            if len(value_list) <= 1:
                result_list.append("%s=%s" % (value_list[0], value_list[0]))
            else:
                result_list = dfs(value_list, result_list)
            print(result_list)
        return


if __name__ == '__main__':
    solution = Solution()
    solution.fun()
