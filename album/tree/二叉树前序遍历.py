"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
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
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

        ans = []
        dfs(root)
        return ans

    def preorderTraversal_loop(self, root):
        res = list()
        if not root:
            return res

        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

if __name__ == '__main__':
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)

    solution = Solution()
    fun = solution.preorderTraversal(root)
    print(fun)
