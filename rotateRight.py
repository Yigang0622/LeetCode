# LeetCode
# rotateRight 
# Created by Yigang Zhou on 2020/9/20.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 旋转链表
# https://leetcode-cn.com/problems/rotate-list/
from common.linkedListCommon import *


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        len = 0
        h = head
        cycled = False
        x = 0
        while head:
            # print(head.val, len)
            if not cycled:
                len += 1
                if head.next is None:
                    head.next = h
                    cycled = True
                    x = len - k % len

            else:
                x -= 1
                if x == 0:
                    n = head.next
                    head.next = None
                    return n
            head = head.next
        return head


head = generateLinkedList([1, 2, 3, 4, 5])
s = Solution().rotateRight(head, 2)
printLinkedList(s)
