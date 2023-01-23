struct Solution {}

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut dq = std::collections::VecDeque::new();
        for ss in s.chars() {
            match ss {
                ss if ss == '(' || ss == '{' || ss == '[' => {
                    dq.push_back(ss);
                }
                ss if ss == ')' => {
                    let c = dq.pop_back();
                    if c != Some('(') {
                        return false;
                    }
                }
                ss if ss == ']' => {
                    let c = dq.pop_back();
                    if c != Some('[') {
                        return false;
                    }
                }
                ss if ss == '}' => {
                    let c = dq.pop_back();
                    if c != Some('{') {
                        return false;
                    }
                },
                _ => ()
            }
        }
        if !dq.is_empty() {
            return false;
        }
        true
    }
}
fn main() {
    assert_eq!(Solution::is_valid("([)]".to_string()), false);
}
