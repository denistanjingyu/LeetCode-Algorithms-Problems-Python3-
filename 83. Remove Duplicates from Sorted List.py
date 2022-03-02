# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Pointer to head
        curr = head
        
        # While loop continues only if curr node and next node both exist
        # If current node value equals next node value, current's next shifts 1 extra
        # If not, curr remains and keep comparing with next
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head