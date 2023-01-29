use std::{collections::{VecDeque, HashSet}, hash::Hash};

struct Solution {}

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut ans = 0;
        let mut dq = VecDeque::new();        
        for c in s.chars() {
            dq.push_back(c);
            if !Self::check(dq.iter().collect::<String>()) {
                loop {
                    dq.pop_front();
                    if Self::check(dq.iter().collect::<String>()) {
                        break;
                    }
                }
            }
            ans = ans.max(dq.len());
        }
        ans as i32
    }

    fn check(s: String) -> bool {
        let mut hs= HashSet::new();
        for c in s.chars() {
            if !hs.insert(c) {
                return false
            }
        }
        true
    }
}

fn main() {
    let res = Solution::length_of_longest_substring("bbbbb".to_string());
    println!("{}", res);
}
