// https://leetcode.com/problems/palindrome-number/

use proconio::input;

struct Solution {}
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let s = x.to_string().chars().collect::<Vec<_>>();
        let mut l = 0;
        let mut r = s.len() - 1;
        loop {
            if s[r] != s[l] {
                return false;
            }
            if r - l < 2 {
                break;
            }
            r -= 1;
            l += 1;
        }
        true
    }
}

fn main() {
    input! {
        i: i32
    }
    println!("{}", Solution::is_palindrome(i));
}
