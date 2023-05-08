# Definition for singly-linked list.
from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = defaultdict(lambda: False)
        while head is not None and (head := head.next) is not None:
            if d[head]:
                return True
            else:
                d[head] = True
        else:
            return False

    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     fast = head
    #     while head and fast.next and (head := head.next) and (fast := fast.next.next):
    #         if head == fast:
    #             return True
    #     return False
