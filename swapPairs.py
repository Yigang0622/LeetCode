# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from common.linkedListCommon import *

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            n1 = cur.next
            n2 = cur.next.next
            cur.next = n2
            n1.next = n2.next
            n2.next = n1
            cur = n1

        return dummy.next


head = generateLinkedList([1,2,3,4])
s = Solution().swapPairs(head)