class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printLinkedList(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next

n = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n.next = n2
n2.next = n3
n3.next = n4
