"""
NC5 二叉树根节点到叶子节点的所有路径和

给定一个仅包含数字0-9 0−9 的二叉树，每一条从根节点到叶子节点的路径都可以用一个数字表示。
例如根节点到叶子节点的一条路径是1\to 2\to 31→2→3,那么这条路径就用 123 123 来代替。
找出根节点到叶子节点的所有路径表示的数字之和
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        ans = 0

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
            ans += int(path)
        return ans


if __name__ == '__main__':
    # 树
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)
    solution = Solution()
    fun = solution.binaryTreePaths(root)
    print(fun)
