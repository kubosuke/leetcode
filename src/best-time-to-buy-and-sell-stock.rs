struct Solution {}

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut min = prices[0];

        for i in 1..prices.len() {
            ans = ans.max(prices[i] - min);
            min = min.min(prices[i]);
        }
        ans
    }
}
fn main() {}

