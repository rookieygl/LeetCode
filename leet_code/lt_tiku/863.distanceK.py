"""
863. 二叉树中所有距离为 K 的结点
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def distanceK(self, root, target, k):
        # 存储子节点和父节点的关联
        node_parent = dict()

        def dfs_find_parent(node) -> None:
            if node:
                if node.left:
                    node_parent[node.left] = node
                if node.right:
                    node_parent[node.right] = node
                dfs_find_parent(node.left)
                dfs_find_parent(node.right)

        # DFS查找父节点，不存储根节点
        dfs_find_parent(root)

        # 从target出发DFS查找，所有深度为K的节点
        def dfs_find_res(node, prev, cur_dist):
            if node:
                if cur_dist == k:
                    res.append(node.val)
                    return
                if node.left != prev:
                    dfs_find_res(node.left, node, cur_dist + 1)
                if node.right != prev:
                    dfs_find_res(node.right, node, cur_dist + 1)
                if node in node_parent and node_parent[node] != prev:
                    dfs_find_res(node_parent[node], node, cur_dist + 1)

        res = []
        dfs_find_res(target, None, 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node4, node5)
    node2 = TreeNode(2)
    root = TreeNode(1, node2, node3)
    fun = solution.distanceK(root, node3, 2)
    print(fun)
