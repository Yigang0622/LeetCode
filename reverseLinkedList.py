from jianzhi_offer.linkedList.common import *

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        printLinkedList(head)
        current = None
        previous = head
        while current is not None:
            previous.next = current
            current = previous
            previous = previous.next

        printLinkedList(previous)

n = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n.next = n2
n2.next = n3
n3.next = n4
Solution().reverseList(n)