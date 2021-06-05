"""
相交链表
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        return True


if __name__ == '__main__':
    node4 = ListNode(4, None)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    headA = ListNode(1, node2)

    headB = ListNode(5, node3)
    solution = Solution()
    fun = solution.getIntersectionNode(headA, headB)
    print(fun)
