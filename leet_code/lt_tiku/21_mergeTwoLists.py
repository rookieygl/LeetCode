"""
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
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
    node13 = ListNode(11, None)
    node12 = ListNode(8, node13)
    node1 = ListNode(2, node12)

    node23 = ListNode(18, None)
    node22 = ListNode(10, node23)
    node2 = ListNode(5, node22)
    solution = Solution()
    fun = solution.mergeTwoLists(node1, node2)
    while fun.next:
        print(fun.val)
        fun = fun.next
