"""
剑指 Offer 52. 两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共节点。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 双指针
    def getIntersectionNode_doblePoint(self, headA, headB):
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:  # 不相交会，会同时达到headA+headB的位置，同时为null
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA

    # hash表 内存大
    def getIntersectionNode_hash(self, headA, headB):
        pS = set()
        pA, pB = headA, headB
        while pA:
            pS.add(pA)
            pA = pA.next
        while pB:
            if pB in pS:
                return pB
            pB = pB.next
        return None


if __name__ == '__main__':
    solution = Solution()
    node13 = ListNode(3, None)
    node12 = ListNode(4, node13)
    node1 = ListNode(2, node12)

    node22 = ListNode(6, node12)
    node2 = ListNode(5, node22)
    fun = solution.getIntersectionNode_hash(node1, node2)
    if fun:
        print(fun.val)
