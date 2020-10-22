# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common.linkedListCommon import *


class Solution:

    # 分成两半，第二半倒转，第一条第一个->第二条第一个->第一条第二个->第二条第一个....
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        # printLinkedList(head)
        second = self.reverseLinkedList(second)
        # printLinkedList(second)

        first_current = head
        second_current = second
        while first_current:
            temp = first_current.next
            first_current.next = second_current
            first_current = temp
            temp_2 = None
            if second_current:
                temp_2 = second_current.next
                second_current.next = temp
            second_current = temp_2
            # printLinkedList(head)


    def reverseLinkedList(self, head) -> ListNode:
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


head = generateLinkedList([1, 2, 3, 4,5,6])
s = Solution().reorderList(head)
printLinkedList(head)
