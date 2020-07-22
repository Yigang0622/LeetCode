from jianzhi_offer.linkedList.common import *

# 回文链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        printLinkedList(head)
        count = 0
        while head:
            arr.append(head.val)
            head = head.next
            count += 1
        if count == 1:
            return True
        half = int(count/2)
        for i in range(half):
            if arr[i] != arr.pop():
                return False
        return True

n = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n4 = ListNode(1)
n.next = n2
n2.next = n3
n3.next = n4
Solution().isPalindrome(n)