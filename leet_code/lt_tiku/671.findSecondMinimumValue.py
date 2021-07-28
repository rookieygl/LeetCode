"""
671. 二叉树中第二小的节点
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        ans, root_value = -1, root.val

        def dfs(node):
            nonlocal ans
            if not node:
                return
            if ans != -1 and node.val >= ans:  # ans已经找到，并且node的值大于ans 只要第二小
                return
            if node.val > root_value:
                ans = node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans


if __name__ == '__main__':
    solution = Solution()
    node5 = TreeNode(3)
    node4 = TreeNode(2)
    node3 = TreeNode(2, node4, node5)
    node2 = TreeNode(1)
    root = TreeNode(1, node2, node3)
    fun = solution.inorderTraversal(root)
    print(fun)
