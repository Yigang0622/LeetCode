# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnnhm6/

from common.linkedListCommon import *

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev



head = generateLinkedList([1,2,3,4,5])
r = Solution().reverseList(head)