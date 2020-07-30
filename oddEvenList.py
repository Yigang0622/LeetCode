from common.linkedListCommon import *

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/31/linked-list/83/


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head:
            return None

        odd_even_head = head
        odd_tail = None
        even_head = None
        even_current = None

        while head is not None:
            if head.next and head.next.next:
                if not even_head:
                    even_head = ListNode(head.next.val)
                    even_current = even_head
                else:
                    even_current.next = ListNode(head.next.val)
                    even_current = even_current.next

                head.next = head.next.next
                head = head.next
            else:
                if head.next:
                    if not even_head:
                        even_head = ListNode(head.next.val)
                    else:
                        even_current.next = ListNode(head.next.val)

                odd_tail = head
                head.next = None
                break

        odd_tail.next = even_head
        return odd_even_head



head = generateLinkedList([1,2,3,4,5,6])
r = Solution().oddEvenList(head)