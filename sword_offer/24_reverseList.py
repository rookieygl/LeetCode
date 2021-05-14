class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 异步指针翻转
    def reverseListDoublePoint(self, head):
        """
        初始化一个指针为None，作为链表起点
        每次循环取出head放到新的指针头，
        head指向head的下一个node 完成翻转
        """
        cur = None
        while head is not None:
            tmp = head.next  # 取出下一个node的剩余链表
            head.next = cur  # 置空下一个node
            cur = head  # head放到临时node
            head = tmp  # 继续循环剩余的node
        return cur

    # 同起点指针翻转
    def reverseListSycDouble(self, head):
        """
        每次循环取出head放到新的指针头（指针初始化为None），
        head指向head的下一个node 完成翻转
        """
        if head is None:
            return
        cur = head
        while head.next is not None:
            tmp = head.next.next
            head.next.next = cur
            cur = head.next
            head.next = tmp
        return cur

    # 同步双指针
    def reverseListRecursion(self, head, a):
        """
        递归翻转
        取到最后一个元素，
        递归从最后一个元素开始指向上一个元素
        """
        if head is None or head.next is None:
            return head
        rec = self.reverseListRecursion(head.next, a)
        head.next.next = head
        head.next = None
        return rec


if __name__ == '__main__':
    node3 = ListNode(4, None)
    node2 = ListNode(3, node3)
    node1 = ListNode(2, node2)
    node = ListNode(1, node1)
    solution = Solution()
    # reverse_head = solution.reverseListDoublePoint(node)
    reverse_head = solution.reverseListRecursion(node, 0)

    while reverse_head is not None:
        # print(reverse_head.val)
        reverse_head = reverse_head.next
