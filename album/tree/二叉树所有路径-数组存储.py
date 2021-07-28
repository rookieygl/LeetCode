"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。数组形式记录路径
说明: 叶子节点是指没有子节点的节点。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        ans, path = [], []

        def dfs(node, path):
            if node:
                path.append(node.val)
                if not node.left and not node.right:
                    ans.append(path[:])
                dfs(node.left, path)
                dfs(node.right, path)
                path.pop()

        dfs(root, path)
        return ans


if __name__ == '__main__':
    # 树
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)
    solution = Solution()
    fun = solution.binaryTreePaths(root)
    print(fun)
