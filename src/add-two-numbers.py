from typing import Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(
		self, l1: Optional[ListNode], l2: Optional[ListNode]
	) -> Optional[ListNode]:
		head = ListNode()
		cur = head
		carry = 0
		while True:
			if l1 is None and l2 is None:
				if carry > 0:
					n = ListNode(val=carry)
					cur.next = n
					cur = n
				break
			v1 = l1.val if l1 is not None else 0
			v2 = l2.val if l2 is not None else 0
			n = ListNode(val=(v1 + v2 + carry)%10)
			carry = (v1 + v2 + carry) // 10
			cur.next = n
			cur = n
			l1 = l1.next if l1 is not None else None
			l2 = l2.next if l2 is not None else None
		return head.next
