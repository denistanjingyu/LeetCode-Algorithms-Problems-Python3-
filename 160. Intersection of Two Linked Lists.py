# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Set pointers to both heads to retain original structure
        pointer_A, pointer_B = headA, headB
        
        # Update both pointers till they meet or return null
        while pointer_A is not pointer_B:
            pointer_A = pointer_A.next if pointer_A else headB
            pointer_B = pointer_B.next if pointer_B else headA
        
        return pointer_A