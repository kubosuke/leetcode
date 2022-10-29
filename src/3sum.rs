// https://leetcode.com/problems/3sum/
struct Solution {}

use std::collections::HashSet;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let v = {
            let mut v = nums.clone();
            v.sort();
            v
        };

        let mut hs = HashSet::new();
        
        for i in 0..v.len() - 1 {
            let mut left = i + 1;
            let mut right = v.len() - 1;
            while left < right {
                match v[i] + v[left] + v[right] {
                    0 => {
                        hs.insert(vec![v[i], v[left], v[right]]);
                        left += 1;
                        right -= 1;
                    }
                    s if s > 0 => {
                        right -= 1;
                    }
                    s if s < 0 => {
                        left += 1;
                    }
                    _ => (),
                }
            }
        }
        hs.into_iter().collect()
    }
}

fn main() {
    let v = vec![-2, 0, 1, 1, 2];
    println!("{:?}", Solution::three_sum(v));
}
