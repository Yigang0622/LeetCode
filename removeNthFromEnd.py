# LeetCode
# removeNthFromEnd 
# Created by Yigang Zhou on 2020/7/22.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printLinkedList(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        arr = []
        while head is not None:
            arr.append(head)
            head = head.next

        if len(arr) == 1:
            return []

        i = len(arr) - n - 1
        if i == -1:
            printLinkedList(arr[1])
            return arr[1]
        else:
            arr[i].next = arr[i].next.next
            printLinkedList(arr[0])
            return arr[0]


n = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n.next = n2
n2.next = n3
n3.next = n4

s = Solution().removeNthFromEnd(n,4)
