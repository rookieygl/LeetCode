"""
94. 二叉树的中序遍历
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 中序递归
    def inorderTraversal_recursion(self, root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        ans = []
        dfs(root)
        return ans

    # 中序迭代
    def inorderTraversal_loop(self, root):
        ans = []
        stk = []
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            ans.append(root.val)
            root = root.right
        return ans


if __name__ == '__main__':
    solution = Solution()
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    root = TreeNode(1, node2, node3)
    fun = solution.inorderTraversal_loop(root)
    print(fun)
