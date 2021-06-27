"""
删除链表的倒数第 N 个结点 N>1

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？
Definition for singly-linked list.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 计算链表长度
    def removeNthFromEnd_length(self, head, n):
        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    # 栈
    def removeNthFromEnd_stack(self, head, n):
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        for i in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next

    def removeNthFromEnd_doublePonit(self, head, n):

        dummy, first = ListNode(0, head), head
        # 切记 second = dummy，否则删除无效
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


if __name__ == '__main__':
    node4 = ListNode(5, None)
    node3 = ListNode(4, node4)
    node2 = ListNode(3, node3)
    node1 = ListNode(2, node2)
    node = ListNode(1, node1)
    solution = Solution()
    fun = solution.removeNthFromEnd_doublePonit(node, 2)
    delList = list()
    while fun:
        delList.append(fun.val)
        fun = fun.next
    print(delList)
    # print("".join(delList)) # join 只能用于字符串序列
