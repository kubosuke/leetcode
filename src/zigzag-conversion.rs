// https://leetcode.com/problems/zigzag-conversion/

use std::vec;

struct Solution {}

impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        // corner
        if s.len() < 3 || num_rows == 1 {
            return s
        }

        let s = s.chars().collect::<Vec<char>>();
        let mut ans = vec![];
        for row in 0..num_rows {
            for col in 0.. {
                let ccol = row + ((2 * num_rows) - 2) * col;
                if !(row == 0 || row == num_rows - 1 || ccol < 2 * row) {
                    if ccol - 2 * row >= s.len() as i32 {
                        break;
                    }
                    ans.push(s[(ccol - 2 * row) as usize]);
                }
                if ccol >= s.len() as i32 {
                    break;
                }
                ans.push(s[ccol as usize]);
            }            
        }
        ans.iter().collect::<String>()        
    }
}

fn main() {
    let s = "A".to_string();
    let num_rows = 1;
    println!("{}", Solution::convert(s, num_rows));
}
