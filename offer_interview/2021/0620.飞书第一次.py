"""
1、实现字典树
2、合并k个链表
3、合并2个链表
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 1、实现字典树

    # 2、合并k个链表
    def mergeKLists(self, lists):
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        if l > r:
            return None
        mid = (l + r) // 2
        return self.mergeTwoLists(self.merge(lists, l, mid), self.merge(lists, mid + 1, r))

    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 if l1 else l2
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
    solution = Solution()
    fun = solution.mergeKLists(1)
    print(fun)
