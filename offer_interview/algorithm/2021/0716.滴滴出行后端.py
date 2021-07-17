"""
1、写个单例
2、合并有序链表
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeList(self, node1, node2):
        mergeNode = ListNode(-1)
        temNode = mergeNode
        while node1 and node2:
            if node1.val < node2.val:
                temNode.next = node1
                node1 = node1.next
            else:
                temNode.next = node2
                node2 = node2.next
            temNode = temNode.next
        if node1 is not None:
            temNode.next = node1
        else:
            temNode.next = node2
        return mergeNode.next


if __name__ == '__main__':
    solution = Solution()
    node12 = ListNode(4, None)
    node1 = ListNode(2, node12)

    node22 = ListNode(3, None)
    node2 = ListNode(1, node22)

    fun = solution.mergeList(node1, node2)
    while fun:
        print(fun.val)
        fun = fun.next
