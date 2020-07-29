# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/31/linked-list/84/
from common.linkedListCommon import *


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        nodeA = headA
        nodeB = headB
        while(nodeA !=nodeB):
            if nodeA:
                nodeA = nodeA.next
            else:
                nodeA = headB

            if nodeB:
                nodeB = nodeB.next
            else:
                nodeB = headA

        return nodeA

