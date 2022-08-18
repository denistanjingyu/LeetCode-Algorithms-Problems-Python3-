# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check_list = []
        curr = head

        while curr:
            check_list.append(curr.val)
            curr = curr.next

        return check_list == check_list[::-1]