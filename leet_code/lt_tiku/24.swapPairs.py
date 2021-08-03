"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs_recursion(self, head):
        if not head or not head.next:
            return head

        newHead = head.next  # 获取当前的下一个节点
        head.next = self.swapPairs_recursion(newHead.next)
        newHead.next = head  # 下一个节指向当前节点
        return newHead

    def swapPairs_loop(self, head):
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next


if __name__ == '__main__':
    solution = Solution()
    node4 = ListNode(4, None)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    fun = solution.swapPairs_recursion(node1)
    while fun:
        print(fun.val)
        fun = fun.next
