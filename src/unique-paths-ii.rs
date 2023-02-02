struct Solution {}

impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let m = obstacle_grid[0].len();
        let n = obstacle_grid.len();
        let mut dp = vec![vec![0; m]; n];
        if obstacle_grid[0][0] == 1 {
            return 0;
        }

        for i in 0..m {
            match obstacle_grid[0][i] {
                1 => break,
                _ => {
                    dp[0][i] = 1;
                }
            }
        }
        for i in 0..n {
            match obstacle_grid[i][0] {
                1 => break,
                _ => {
                    dp[i][0] = 1;
                }
            }
        }
        if 0 < m && 0 < n {
            for i in 1..m {
                for j in 1..n {
                    if obstacle_grid[j][i] != 1 {
                        dp[j][i] = dp[j - 1][i] + dp[j][i - 1];
                    }
                }
            }
        }
        dp[n - 1][m - 1] as i32
    }
}

fn main() {
    println!(
        "{}",
        Solution::unique_paths_with_obstacles(vec![vec![0, 0], vec![1, 1], vec![0, 0]])
    );
}
