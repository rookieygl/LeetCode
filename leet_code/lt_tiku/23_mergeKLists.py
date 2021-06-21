"""
合并K个升序链表

给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        if l > r:
            return None
        mid = (l + r) // 2
        return self.mergeTwoLists(self.merge(lists, l, mid), self.merge(lists, mid + 1, r))

    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 if l1 else l2
        merge = ListNode(-1)
        prev = merge
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 is not None else l2
        return merge.next


if __name__ == '__main__':
    solution = Solution()
    node13 = ListNode(11, None)
    node12 = ListNode(8, node13)
    node1 = ListNode(2, node12)

    node23 = ListNode(18, None)
    node22 = ListNode(10, node23)
    node2 = ListNode(5, node22)

    fun = solution.mergeKLists([node1, node2])
    while fun.next:
        print(fun.val)
        fun = fun.next
