"""
相交链表
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 哈希表
    def getIntersectionNode_hash(self, headA, headB):
        nodeSet = set()
        while headA:
            nodeSet.add(headA)
            headA = headA.next

        while headB:
            if headB in nodeSet:
                return headB
            headB = headB.next
        return None

    # 双指针 性能更好
    def getIntersectionNode_doblePoint(self, headA, headB):
        if not headA or not headB:
            return None
        # pa pb的交换 不影响head
        pa, pb = headA, headB
        while pa != pb:
            pa = headB if pa == None else pa.next
            pb = headA if pb == None else pb.next
        return pa


if __name__ == '__main__':
    node4 = ListNode(4, None)
    headC = ListNode(3, node4)

    node2 = ListNode(2, headC)
    headA = ListNode(1, node2)

    headB = ListNode(5, headC)
    solution = Solution()
    fun = solution.getIntersectionNode_doblePoint(headA, headB)
    print(fun.val)
