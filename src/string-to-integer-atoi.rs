// https://leetcode.com/problems/string-to-integer-atoi/

use std::vec;

use proconio::input;

struct Solution {}

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let mut v = vec![];
        for c in s.chars() {
            match c {
                cc if cc == '+' || cc == '-' => {
                    if v.is_empty() {
                        v.push(cc);
                    } else {
                        break;
                    }
                },
                cc if '0' <= cc && cc <= '9' => {
                    v.push(cc)
                },
                ' ' => {
                    if v.is_empty() {
                        continue;
                    } else {
                        break;
                    }
                },
                _ => {
                    if v.is_empty() {
                        break;
                    } else {
                        break;
                    }
                }
            }
        }
        if v.is_empty() {
            v.push('0');
        }
        println!("{:?}", v);
        match v.iter().collect::<String>().parse::<i32>() {
            Ok(i) => return i,
            Err(_) => {
                if v[0] == '-' {
                    if v.len() == 1 {
                        return 0;
                    }
                    return i32::MIN;
                } else {
                    if v.len() == 1 {
                        return 0;
                    }                    
                    return i32::MAX;
                }
            }
        }
    }
}

fn main() {
    input! {
        s: String
    }
    println!("{}", Solution::my_atoi(s));
}
