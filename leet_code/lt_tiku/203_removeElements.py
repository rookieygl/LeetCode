"""
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements_recursion(self, head, val):
        if not head:
            return head
        head.next = self.removeElements_recursion(head.next, val)
        return head.next if head.val == val else head

    # 迭代
    def removeElements_cycle(self, head, val):
        dummy = ListNode(0, head)
        new = dummy
        while new.next:
            if new.next.val == val:
                new.next = new.next.next
                continue
            new = new.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    node4 = ListNode(2, None)
    node3 = ListNode(2, node4)
    node2 = ListNode(2, node3)
    headA = ListNode(1, node2)
    fun = solution.removeElements_recursion(headA, 2)
    while fun:
        print(fun.val)
        fun = fun.next
