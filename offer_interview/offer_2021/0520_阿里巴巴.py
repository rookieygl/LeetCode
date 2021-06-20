"""
报数退出
标号1-n的n个人首尾相接，1到3报数，报到3的退出，求最后一个人的标号
"""


class Solution(object):
    def callExit(self, n, exit):
        exitArr = [i for i in range(1, n + 1)]
        print(exitArr)
        index, exitSum, exitCall = 0, 0, 0
        while True:
            # 循环
            if index > n - 1:
                index = 0
            if exitArr[index] > 0:
                exitCall += 1

            if exitCall == exit and exitSum < n - 1:
                exitArr[index] = 0
                exitCall = 0
                exitSum += 1
            elif exitSum == n - 1:
                return exitArr[index]
            index += 1


if __name__ == '__main__':
    solution = Solution()
    call_exit = solution.callExit(3, 3)
    print(call_exit)
