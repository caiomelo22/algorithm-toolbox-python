# Time Complexity O(n)
# Space Complexity O(1)

from typing import Optional
from src.linked_list.node import ListNode

def hasCycle(head: Optional[ListNode]) -> bool:
    fast = head
    slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
        if fast == slow:
            return True

    return False
    