class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head, tail = None, None
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                val1 = 0
            else:
                val1 = l1.val

            if l1 is None:
                val2 = 0
            else:
                val2 = l2.val

            count = val1 + val2 + carry
            if head is None:
                head = tail = ListNode(count % 10, None)
            else:
                tail.next = ListNode(count % 10, None)
                tail = tail.next
            carry = int(count / 10)
            l1 = l1.next
            l2 = l2.next
        if carry > 0:
            tail.next = ListNode(carry, None)
        return head


if __name__ == '__main__':
    node13 = ListNode(3, None)
    node12 = ListNode(4, node13)
    node1 = ListNode(2, node12)

    node23 = ListNode(4, None)
    node22 = ListNode(6, node23)
    node2 = ListNode(5, node22)
    solution = Solution()
    numbers = solution.addTwoNumbers(node1, node2)
    while numbers is not None:
        print(numbers.val)
        numbers = numbers.next
