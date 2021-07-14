"""
206. 反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return
        rec = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rec


if __name__ == '__main__':
    node3 = ListNode(4, None)
    node2 = ListNode(3, node3)
    node1 = ListNode(2, node2)
    node = ListNode(1, node1)
    solution = Solution()
    fun = solution.reverseList(node)
    while fun:
        print(fun.val)
        fun = fun.next
