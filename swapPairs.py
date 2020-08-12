# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from common.linkedListCommon import *

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        printLinkedList(head)
        x = head.next

        cur = head
        while cur:
            print('!')
            temp = cur.next
            cur.next = temp.next
            temp.next = cur
            printLinkedList(temp)

            cur = cur.next


        printLinkedList(x)

        return head


head = generateLinkedList([1,2,3,4])
s = Solution().swapPairs(head)