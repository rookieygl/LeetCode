"""
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
    def pathSum_dfs(self, root, targetSum):
        ans, path = [], []

        def dfs(root, targetSum):
            if not root:
                return
            path.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:  # 只记录符合的路径
                ans.append(path[:])  # 传入path的copy，防止path一直追加元素
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()  # 走过的路径移除出去

        dfs(root, targetSum)
        return ans

    # 广度搜索
    def pathSum_bfs(self, root, targetSum):
        ans = []
        if not root:
            return ans
        parent = defaultdict(lambda: None)

        def getPath(node):
            tmp = []
            while node:
                tmp.append(node.val)
                node = parent[node]
            ans.append(tmp[::-1])

        que_node = deque([root])
        que_total = deque([0])
        while que_node:
            node = que_node.popleft()
            rec = que_total.popleft() + node.val
            if not node.left and not node.right:
                if rec == targetSum:
                    getPath(node)
            else:
                if node.left:
                    parent[node.left] = node
                    que_node.append(node.left)
                    que_total.append(rec)
                if node.right:
                    parent[node.right] = node
                    que_node.append(node.right)
                    que_total.append(rec)
        return ans


if __name__ == '__main__':
    solution = Solution()
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node4, node5)
    node2 = TreeNode(2)
    root = TreeNode(1, node2, node3)
    fun = solution.pathSum_dfs(root, 3)
    print(fun)
