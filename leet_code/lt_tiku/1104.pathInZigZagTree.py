"""
863. 二叉树中所有距离为 K 的结点
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathInZigZagTree(self, label):
        def getReverse(label, row):
            return (1 << row - 1) + (1 << row) - 1 - label

        row, rowStart = 1, 1
        while rowStart * 2 <= label:
            row += 1
            rowStart *= 2
        if row % 2 == 0:
            label = getReverse(label, row)
        path = list()
        while row > 0:
            if row % 2 == 0:
                path.append(getReverse(label, row))
            else:
                path.append(label)
            row -= 1
            label >>= 1
        # reversed(path) 翻转后是一个迭代集合，需要转成list
        return list(reversed(path))


if __name__ == '__main__':
    solution = Solution()
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node4, node5)
    node2 = TreeNode(2)
    root = TreeNode(1, node2, node3)
    fun = solution.pathInZigZagTree(2)
    print(fun)
