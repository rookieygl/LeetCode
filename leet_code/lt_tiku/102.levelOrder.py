"""
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        ans = []
        dfs(root)
        return ans


if __name__ == '__main__':
    solution = Solution()
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    root = TreeNode(1, node2, node3)
    fun = solution.inorderTraversal(root)
    print(fun)
