# LeetCode
# linkedListCommon 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printLinkedList(head: ListNode):
    while head is not None:
        if head.next is None:
            print(head.val)
        else:
            print(head.val, '-> ', end='')
        head = head.next


def generateLinkedList(arr: List[int]):
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        current.next = node
        current = node
    return head

