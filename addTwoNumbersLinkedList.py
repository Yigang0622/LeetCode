# LeetCode
# addTwoNumbersLinkedList 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.
# https://leetcode-cn.com/problems/sum-lists-lcci/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common.linkedListCommon import *

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        extra = 0
        ml1 = l1
        ml2 = l2

        head = None
        cur = head

        while ml1 or ml2:

            two_sum = 0

            if ml1 is None and ml2:
                two_sum = extra + ml2.val

            if ml2 is None and ml1:
                two_sum = extra + ml1.val

            if ml1 and ml2:
                two_sum = extra + ml1.val + ml2.val

            if two_sum >= 10:
                extra = int(two_sum / 10)
                two_sum = two_sum % 10
            else:
                two_sum = two_sum
                extra = 0
            print(extra, two_sum)

            if cur is None:
                cur = ListNode(two_sum)
                head = cur
            else:
                cur.next = ListNode(two_sum)
                cur = cur.next

            if ml1:
                ml1 = ml1.next
            else:
                ml1 = None

            if ml2:
                ml2 = ml2.next
            else:
                ml2 = None

        if extra > 0:
            cur.next = ListNode(extra)

        return head

l1 = generateLinkedList([5])
l2 = generateLinkedList([7])
r = Solution().addTwoNumbers(l1,l2)
printLinkedList(r)