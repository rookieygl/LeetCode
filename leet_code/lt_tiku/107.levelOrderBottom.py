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
    # 循环取出树的节点放入队列
    def inorderTraversal_loop(self, root):
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                r = queue.pop(0)
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            ans.append(tmp)
        return ans[::-1]

    # 层次递归
    def inorderTraversal_recursion(self, root):
        if not root:
            return []
        ans = []

        def dfs(index, node):
            if len(ans) < index:
                ans.append([])
            ans[index - 1].append(node.val)
            if node.left:
                dfs(index + 1, node.left)
            if node.right:
                dfs(index + 1, node.right)

        dfs(1, root)
        return ans[::-1]


if __name__ == '__main__':
    solution = Solution()
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node4, node5)
    node2 = TreeNode(2)
    root = TreeNode(1, node2, node3)
    fun = solution.levelOrderBottom(root)
    print(fun)
