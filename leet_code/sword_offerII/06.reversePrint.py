"""
剑指 Offer 06. 从尾到头打印链表
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reversePrint(self, head):
        valL = []
        while head:
            valL.append(head.val)
            head = head.next
        newVal = []
        while valL:
            newVal.append(valL.pop())  # pop默认索引位置-1，最后一个元素
        return newVal


if __name__ == '__main__':
    solution = Solution()
    node3 = ListNode(4, None)
    node2 = ListNode(3, node3)
    node1 = ListNode(2, node2)
    node = ListNode(1, node1)
    fun = solution.reversePrint(node)
    print(fun)
