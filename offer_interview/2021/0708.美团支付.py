"""
1、二叉树路径数字
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        def dfs(node, s):
            if node:
                s += str(node.val)
                if not node.left and not node.right:
                    paths.append(s)
                dfs(node.left, s)
                dfs(node.right, s)

        paths = []
        dfs(root, "")
        for path in paths:
            print(path)
        return 0


if __name__ == '__main__':
    # 树
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)
    solution = Solution()
    fun = solution.binaryTreePaths(root)
    print(fun)
