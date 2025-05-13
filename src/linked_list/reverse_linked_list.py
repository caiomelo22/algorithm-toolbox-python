# Time Complexity O(n)
# Space Complexity O(1)

from typing import Optional
from src.linked_list.node import ListNode


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        temp = curr.next

        curr.next = prev
        prev = curr

        curr = temp

    return prev
    