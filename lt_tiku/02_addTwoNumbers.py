class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = tail = ListNode(0, None)
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next

            if l2 is None:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next

            count = val1 + val2 + carry
            carry = int(count / 10)
            # 存储链表
            tail.next = ListNode(count % 10, None)
            tail = tail.next
        if carry > 0:
            tail.next = ListNode(carry, None)
        return head.next


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
