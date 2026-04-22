class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a placeholder to start the new list
        dummy = ListNode()
        cur = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        # Attach whichever list still has nodes left
        cur.next = list1 if list1 else list2
        
        # Return the actual start (skipping the dummy)
        return dummy.next
        