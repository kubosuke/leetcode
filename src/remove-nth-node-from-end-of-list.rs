// https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/2754858/Rust-100-beats

struct Solution {}

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut head = head;
        let mut fast = head.clone();
        let mut slow = head.as_mut();
        for _ in 0..n {
            fast = fast.unwrap().next;
        }
        if fast == None {
            return head.unwrap().next;
        }
        while fast.clone().unwrap().next != None {
            fast = fast.unwrap().next;
            slow = slow.unwrap().next.as_mut();
        }
        slow.as_mut().unwrap().next = slow.as_mut().unwrap().next.as_mut().unwrap().next.take();
        head        
    }
}
fn main() {}
