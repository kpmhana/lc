""" p = []

print(p)
print(not p)
 """


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


""" list3 = ListNode(None, None)
head3 = list3

list3.val = 3
list3.next = ListNode(None, None)
list3 = list3.next

list3.val = 2
list3.next = ListNode(None, None)
list3 = list3.next

list3.val = 1
list3.next = None
list3 = list3.next


while(head3):
    print(head3.val)
    head3 = head3.next

 """

list3 = None
head3 = list3

list3 = ListNode(1, None)
head3 = list3


list3.next = ListNode(2, None)
list3 = list3.next

list3.next = ListNode(3, None)
list3 = list3.next


while(head3):
    print(head3.val)
    head3 = head3.next

