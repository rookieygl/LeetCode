"""
1、二叉树前序和中序遍历，写出后续遍历
2、概率问题 54张扑克，大小王在一起的概率
3、两数相加，先翻转，后相加，难度不大
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        return 0


if __name__ == '__main__':
    solution = Solution()
    fun = solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(fun)
