# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common.linkedListCommon import *


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # printLinkedList(head)
        head_copy = head

        seg_head = None
        before_head = None
        prev = None
        i = 1
        while i <= n:
            print(i)
            if i == m:
                before_head = prev
                seg_head = head
                # print('before_head set to', before_head.val)
                # print('seg_head set to', seg_head.val)
                # print('prev set to', prev.val)
                prev = head
                head = head.next
            elif m < i <= n:
                temp = head.next
                head.next = prev
                # print('prev', prev.val)
                # print('temp', head.val,'temp.next', head.next.val)
                prev = head
                head = temp
                # print('head set to', head.val)
            else:
                prev = head
                # print("prev setttt", prev.val)
                head = head.next

            i += 1

        seg_head.next = head
        if before_head:
            before_head.next = prev
            return head_copy
        else:
            return prev



head = generateLinkedList([1, 2, 3, 4, 5])
m = 1
n = 3
r = Solution().reverseBetween(head, m, n)
print()
printLinkedList(r)
