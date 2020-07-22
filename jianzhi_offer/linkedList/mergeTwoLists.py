from jianzhi_offer.linkedList.common import *

class Solution(object):

    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


n = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n.next = n2
n2.next = n3
n3.next = n4

a = ListNode(2)
a2 = ListNode(3)
a3 = ListNode(6)
a4 = ListNode(7)
a.next = a2
a2.next = a3
a3.next = a4

Solution().mergeTwoLists(n,a)
