"""
1736. 替换隐藏数字得到的最晚时间

给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。
有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。
替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。
"""


class Solution(object):
    def maximumTime(self, time):
        if time[0] == "?":
            time[0] = '1' if '4' <= time[1] <= '9' else '2'
        if time[1] == "?":
            time[1] = '9' if time[0] == '1' else '4'
        if time[2] == "?":
            time[2] = '5'
        if time[3] == "?":
            time[3] = '9'
        return time


if __name__ == '__main__':
    solution = Solution()
    fun = solution.maximumTime('2?:?0')
    print(fun)
