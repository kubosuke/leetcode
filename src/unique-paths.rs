struct Solution {}

impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let n = n as usize;
        let m = m as usize;
        let mut dp = vec![vec![0; m]; n];
        for i in 0..n {
            dp[i][0] = 1;
        }
        for i in 0..m {
            dp[0][i] = 1;
        }
        for i in 1..n {
            for j in 1..m {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        dp[n-1][m-1]
    }
}

fn main() {}
