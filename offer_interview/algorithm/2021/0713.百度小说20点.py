"""
1、遍历二叉树的左子树
2、最大子序和
3、红包随机分发
"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 1、遍历二叉树的左子树
    def traversingLeftLeaves(self, root):
        if not root:
            return 0

        isLeafNode = lambda node: not node.left and not node.right
        q = collections.deque([root])
        ans = []

        while q:
            node = q.popleft()
            if node.left:
                if isLeafNode(node.left):
                    ans.append(node.left.val)
                else:
                    q.append(node.left)
            if node.right:
                if not isLeafNode(node.right):
                    q.append(node.right)

        return ans

    # 2、最大子序和
    def maxSubArray(self, nums):
        pre, maxAns = 0, nums[0]
        for num in nums:
            pre = max(num, num + pre)
            maxAns = max(maxAns, pre)
        return maxAns


if __name__ == '__main__':
    solution = Solution()
    # fun = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    # print(fun)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node2 = TreeNode(2, node4, None)
    root = TreeNode(1, node2, node3)
    fun = solution.traversingLeftLeaves(root)
    print(fun)
