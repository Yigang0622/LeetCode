# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common.linkedListCommon import *


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        printLinkedList(head)
        head_copy = head
        head = head.next

        seg_head = None
        before_head = None
        prev = None
        i = 1
        while i < n:
            if i == m:
                before_head = prev
                seg_head = head
            elif n < i < m:
                temp = head
                temp.next = prev

            prev = head
            head = head.next
            i += 1

        return head_copy



head = generateLinkedList([1, 2, 3, 4, 5])
m = 2
n = 4
r = Solution().reverseBetween(head, m, n)
