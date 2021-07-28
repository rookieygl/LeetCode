"""
113. 路径总和 II
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。
"""
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 深度搜索
    def hasPathSum_dfs(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum_dfs(root.left, targetSum - root.val) \
               or self.hasPathSum_dfs(root.right, targetSum - root.val)

    # 广度搜索
    def hasPathSum_bfs(self, root, targetSum):
        if not root:
            return False
        que_node = deque([root])
        que_val = deque([root.val])
        while que_node:
            node = que_node.popleft()
            tmp = que_val.popleft()
            if not node.left and not node.right:
                if tmp == targetSum:
                    return True
            if node.left:
                que_node.append(node.left)
                que_val.append(node.left.val + tmp)
            if node.right:
                que_node.append(node.right)
                que_val.append(node.right.val + tmp)
        return False


if __name__ == '__main__':
    solution = Solution()
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node4, node5)
    node2 = TreeNode(2)
    root = TreeNode(1, node2, node3)
    fun = solution.hasPathSum_bfs(root, 3)
    print(fun)
