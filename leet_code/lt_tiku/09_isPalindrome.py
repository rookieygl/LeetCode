"""
回文数
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
"""


class Solution(object):
    # 本人的 觉得好垃圾啊
    def isPalindromeMe(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x < 10:
            return True

        pali = 0
        len1 = len(str(x))
        numLen = (len1 + 1) // 2
        for i in range(numLen):
            digit = x % 10
            if i < len1 // 2:
                x //= 10
            pali = pali * 10 + digit
        if pali == x:
            return True
        return False

    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x < 10:
            return True
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x /= 10
        return x == revertedNumber or x == revertedNumber / 10


if __name__ == '__main__':
    solution = Solution()
    palindrome = solution.isPalindrome(8)
    print(palindrome)
