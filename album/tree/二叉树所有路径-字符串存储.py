"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。字符串形式记录路径
说明: 叶子节点是指没有子节点的节点。
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
                s += "->"
                dfs(node.left, s)
                dfs(node.right, s)

        paths = []
        dfs(root, "")
        return paths


if __name__ == '__main__':
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)
    solution = Solution()
    fun = solution.binaryTreePaths(root)
    print(fun)
