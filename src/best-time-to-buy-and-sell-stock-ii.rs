use std::vec;

struct Solution {}

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 0..prices.len()-1 {
            let v = prices[i+1] - prices[i]; 
            if v > 0 {
                ans += v;
            }
        }
        ans
    }
}


use itertools::Itertools;
fn main() {
    let v = vec![7,1,5,3,6,4];
}