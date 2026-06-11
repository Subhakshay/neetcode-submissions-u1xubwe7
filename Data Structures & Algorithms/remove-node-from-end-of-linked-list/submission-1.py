# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        Index = count - n

        if Index == 0:
            return head.next
        cur = head
        for i in range(count - 1):
            if (i+1) == Index:
                cur.next = cur.next.next
                
            cur = cur.next
        return head
