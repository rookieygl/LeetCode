class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        while l1 is not None or l2 is not None:

            l1 = l1.next
            l2 = l2.next


if __name__ == '__main__':
    node13 = ListNode(3, None)
    node12 = ListNode(4, node13)
    node1 = ListNode(2, node12)

    node23 = ListNode(4, None)
    node22 = ListNode(6, node23)
    node2 = ListNode(5, node12)
    solution = Solution()
    solution.addTwoNumbers(node1, node2)
