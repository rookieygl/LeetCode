"""
1、二叉树的层序遍历
2、二分查找
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1  # 右边界不能越界
        while left <= right:
            mid = (left + right) // 2  # pivot = left + (right - left) // 2 这样写可以防止溢出，但是Python不会溢出
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1  # 整除会有损失，需要补偿
        return -1

    def inorderTraversal(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            r = queue.pop(0)
            res.append(r.val)
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)
        return res


if __name__ == '__main__':
    solution = Solution()
    fun = solution.search([7, 8, 9, 1, 2], 9)
    print(fun)
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node4, node5)
    node2 = TreeNode(2)
    root = TreeNode(1, node2, node3)
    fun = solution.inorderTraversal(root)
    print(fun)
