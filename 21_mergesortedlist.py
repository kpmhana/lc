class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode(5, ListNode(8, ListNode(15, None)))
list2 = ListNode(1, ListNode(15, ListNode(26, None)))

list3 = ListNode()
head3 = list3

while(list1 and list2):
    if(list1.val <= list2.val):
        list3.next = list1
        list1 = list1.next
                
    else:
        list3.next = list2
        list2 = list2.next

    list3 = list3.next
        
if(list1):
    list3.next = list1
else:
    list3.next = list2
    
while head3.next:
    print(head3.val)
    head3 = head3.next
