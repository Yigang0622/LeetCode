# LeetCode
# deleteDuplicates 
# Created by Yigang Zhou on 2020/11/7.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from common.linkedListCommon import *


# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
# 82. 删除排序链表中的重复元素 II

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        c = head
        prev = None
        while head and head.next:
            if head.val == head.next.val:
                if not prev:
                    head = self.removeElement(head, val=head.val)
                    c = head
                else:
                    prev.next = self.removeElement(head, val=head.val)
                    head = prev
            else:
                prev = head
                head = head.next
        return c


    def removeElement(self, node: ListNode, val):
        head = node
        while head and head.val == val:
            head = head.next
        return head


head = generateLinkedList([1, 1, 2,2, 3, 3, 3, 3, 4, 4, 5,5])
s = Solution().deleteDuplicates(head)
