# LeetCode
# partitionLinkedList 
# Created by Yigang Zhou on 2020/10/7.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 86. 分隔链表
# https://leetcode-cn.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from common.linkedListCommon import *


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # printLinkedList(head)
        if not head:
            return None
        left_current = None
        left_head = left_current
        right_current = None
        right_head = right_current

        while head:
            if head.val < x:
                if not left_current:
                    left_current = ListNode(head.val)
                    left_head = left_current
                else:
                    left_current.next = ListNode(head.val)
                    left_current = left_current.next
            else:
                if not right_current:
                    right_current = ListNode(head.val)
                    right_head = right_current
                else:
                    right_current.next = ListNode(head.val)
                    right_current = right_current.next

            head = head.next

        # printLinkedList(left_head)
        # printLinkedList(right_head)
        if left_current:
            left_current.next = right_head
            return left_head
        else:
            return right_head


head = generateLinkedList([1, 4, 3, 2, 5, 2])
x = 3
r = Solution().partition(head, 3)
printLinkedList(r)