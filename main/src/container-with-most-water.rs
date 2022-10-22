// https://leetcode.com/problems/container-with-most-water/

use proconio::input;

struct Solution {}
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        macro_rules! chmax {
            ($base:expr, $($cmps:expr),+ $(,)*) => {{
                let cmp_max = max!($($cmps),+);
                if $base < cmp_max {
                    $base = cmp_max;
                    true
                } else {
                    false
                }
            }};
        }
        
        macro_rules! max {
            ($a:expr $(,)*) => {{
                $a
            }};
            ($a:expr, $b:expr $(,)*) => {{
                std::cmp::max($a, $b)
            }};
            ($a:expr, $($rest:expr),+ $(,)*) => {{
                std::cmp::max($a, max!($($rest),+))
            }};
        }

        let mut l = 0;
        let mut r = height.len() - 1;
        let mut cur_vol = 0; 
        while r - l > 0 {
            chmax!(cur_vol, height[l].min(height[r]) * (r - l) as i32);
            if height[r] > height[l] {
                l += 1
            } else {
                r -= 1
            }
        }   
        cur_vol                     
    }
}

fn main() {
    let v = vec![1,8,6,2,5,4,8,3,7];
    println!("{}", Solution::max_area(v));

    let v = vec![1,1];
    println!("{}", Solution::max_area(v));
}
