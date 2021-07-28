"""
1、二叉树前序和中序遍历，写出后续遍历
2、概率问题 54张扑克，大小王在一起的概率
3、两数相加，先翻转，后相加，难度不大
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        def recur(root, left, right):
            if left > right:
                return  # 递归终止
            node = TreeNode(preorder[root])  # 建立根节点
            i = dic[preorder[root]]  # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)  # 左子树递归
            node.right = recur(i - left + root + 1, i + 1, right)  # 右子树递归
            return node  # 回溯返回根节点

        dic, preorder = {}, preorder
        dic = {element: i for i, element in enumerate(inorder)}
        return recur(0, 0, len(inorder) - 1)


if __name__ == '__main__':
    solution = Solution()
    fun = solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])


    def inorder(root, ans):
        if not root:
            return ans
        inorder(root.left, ans)
        ans.append(root.val)
        inorder(root.right, ans)


    ans = []
    inorder(fun, ans)
    print(ans)
