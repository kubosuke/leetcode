use std::collections::VecDeque;

struct Solution {}

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut ans = vec![];
        for bit in 0..(1 << n*2) {
            let s = (0..n*2)
                .map(|x| if bit & (1 << x) != 0 { '(' } else { ')' })
                .collect::<String>();
            if Self::ok(s.clone()) {
                ans.push(s);
            }
        }
        ans
    }
    fn ok(s: String) -> bool {
        let mut dq = VecDeque::new();
        for c in s.chars() {
            match c {
                c if c == '(' => dq.push_back(c),
                c if c == ')' => {
                    let v = dq.pop_back();
                    if v.is_none() || v.unwrap() != '(' {
                        return false;
                    }
                }
                _ => return false,
            }
        }
        if !dq.is_empty() {
            return false
        }
        true
    }
}

fn main() {
    println!("{:?}", Solution::generate_parenthesis(3));
}
