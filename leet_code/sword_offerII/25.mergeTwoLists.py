"""
合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 递归 一次传入下一个元素即可
    def mergeTwoLists_recursion(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists_recursion(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_recursion(l1, l2.next)
            return l2

    # 迭代 一次只取一个元素
    def mergeTwoLists_while(self, l1, l2):
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
    fun = solution.mergeTwoLists_while(node1, node2)
    while fun.next:
        print(fun.val)
        fun = fun.next
