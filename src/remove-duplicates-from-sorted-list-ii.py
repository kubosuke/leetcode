# Definition for singly-linked list.
from typing import Optional
from collections import defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev = head.val
        m = defaultdict(lambda: 0)
        ans = None
        tmp = None
        while (cur := head) is not None:
            if prev != cur.val:
                if m[prev] == 1:
                    if ans is None:
                        ans = ListNode(prev)
                        tmp = ans
                    else:
                        tmp.next = ListNode(prev)
                        tmp = tmp.next
            m[cur.val] += 1            
            head = cur.next
            prev = cur.val
        if m[prev] == 1:
            if ans is None:
                ans = ListNode(prev)
                tmp = ans
            else:
                tmp.next = ListNode(prev)
                tmp = tmp.next
        return ans
