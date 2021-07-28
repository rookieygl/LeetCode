"""
145. 二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal_recursion(self, root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)

        ans = []
        dfs(root)
        return ans

    def preorderTraversal_loop(self, root):
        if not root:
            return list()

        res = list()
        stack = list()
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res


if __name__ == '__main__':
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)

    solution = Solution()
    fun = solution.preorderTraversal_loop(root)
    print(fun)
