"""
剑指 Offer 24. 反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 异步指针翻转
    def reverseList_loop(self, head):
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

    # 递归
    def reverseListRecursion(self, head):
        """
        递归翻转
        取到最后一个元素，
        递归从最后一个元素开始指向上一个元素
        """
        if not head or not head.next:
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
    fun = solution.reverseListRecursion(node)

    while fun is not None:
        print(fun.val)
        fun = fun.next
