"""
翻转链表
"""


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
        while head:
            tmp = head.next  # 取出下一个node的剩余链表
            head.next = cur  # cur 挂到head的下一个
            cur = head  # 交换head和next
            head = tmp  # 遍历剩余链表
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
        while head.next:
            tmp = head.next.next
            head.next.next = cur
            cur = head.next
            head.next = tmp
        return cur

    # 递归
    def reverseListRecursion(self, head):
        """
        递归翻转
        取到最后一个元素，
        递归从最后一个元素开始指向上一个元素
        """
        if head is None or head.next is None:
            return head
        rec = self.reverseListRecursion(head.next)
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
    reverse_head = solution.reverseListSycDouble(node)

    while reverse_head is not None:
        print(reverse_head.val)
        reverse_head = reverse_head.next
