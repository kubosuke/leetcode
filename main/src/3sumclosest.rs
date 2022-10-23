// https://leetcode.com/problems/3sum-closest/
struct Solution {}

macro_rules! chmin {
    ($base:expr, $($cmps:expr),+ $(,)*) => {{
        let cmp_min = min!($($cmps),+);
        if $base > cmp_min {
            $base = cmp_min;
            true
        } else {
            false
        }
    }};
}

macro_rules! min {
    ($a:expr $(,)*) => {{
        $a
    }};
    ($a:expr, $b:expr $(,)*) => {{
        std::cmp::min($a, $b)
    }};
    ($a:expr, $($rest:expr),+ $(,)*) => {{
        std::cmp::min($a, min!($($rest),+))
    }};
}

impl Solution {
    pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
        let nums = {
            let mut tmp = nums.clone();
            tmp.sort();
            tmp
        };
        let mut ans = 1000000000;
        let mut buf = 1000000000;
        for i in 0..nums.len() {
            let mut left = i+1;
            let mut right = nums.len() - 1;
            while left < right {
                let s = nums[i] + nums[left] + nums[right];
                if chmin!(buf, (s - target).abs()) {
                    ans = s;
                };
                match s {
                    s if s < target => {
                        left += 1;
                    }
                    s if target < s => {
                        right -= 1;
                    }
                    s if target == s => {
                        return s;
                    }
                    _ => (),
                }
            }
        }
        ans
    }
}

fn main() {
    let v = vec![-1, 2, 1, -4];
    assert_eq!(2, Solution::three_sum_closest(v, 1));
    let v = vec![0, 0, 0];
    assert_eq!(0, Solution::three_sum_closest(v, 1));
}
