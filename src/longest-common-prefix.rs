// https://leetcode.com/problems/longest-common-prefix/

use proconio::input;
use std::collections::HashSet;

struct Solution{}

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut ans = vec![];
        let v = strs.iter().map(|x| x.chars().collect::<Vec<_>>()).collect::<Vec<_>>();
        for i in 0.. {                 
            let mut hs = HashSet::new();
            let mut f = false;
            for vv in v.clone() {
                match &vv.get(i) {
                    Some(vvv) => {
                        hs.insert(**vvv);
                    },
                    _ => {
                        f = true;
                        continue;
                    }
                }
            }
            match hs.len() {
                1 => {
                    if f {
                        break;
                    }
                    ans.push(*hs.iter().collect::<Vec<_>>()[0]);
                },
                _ => break
            }
        }
        ans.iter().collect::<String>()
    }
}

fn main() {
    // input! {
    //     n: i32
    // }
    // let vec = vec!["flower".to_string(),"flow".to_string(),"flight".to_string()];
    let vec = vec!["dog".to_string(),"racecar".to_string(),"car".to_string()];
    let res = Solution::longest_common_prefix(vec);
    println!("{}", res)
}