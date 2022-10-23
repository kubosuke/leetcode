// https://leetcode.com/problems/4sum/

struct Solution {}

impl Solution {
    pub fn four_sum(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        if nums.len() < 4 {
            return vec![];
        }

        let mut res = std::collections::HashSet::new();

        let nums = {
            let mut tmp = nums;
            tmp.sort();
            tmp
        };

        for i in 0..nums.len() - 2 {
            for j in i + 1..nums.len() - 1 {
                let mut left = j + 1;
                let mut right = nums.len() - 1;
                while left < right {
                    let f = {
                        let mut f = false;
                        let f1 = nums[i].checked_add(nums[j]);
                        let f2 = nums[left].checked_add(nums[right]);
                        match (f1, f2) {
                            (Some(x), Some(y)) => match x.checked_add(y) {
                                Some(_) => (),
                                _ => f = true,
                            },
                            _ => f = true,
                        }
                        f
                    };
                    if f {
                        right -= 1;
                    } else {
                        match nums[i] + nums[j] + nums[left] + nums[right] {
                            s if s > target => {
                                right -= 1;
                            }
                            s if s < target => {
                                left += 1;
                            }
                            s if s == target => {
                                res.insert(vec![nums[i], nums[j], nums[left], nums[right]]);
                                left += 1;
                                right -= 1;
                            }
                            _ => (),
                        }
                    }
                }
            }
        }
        res.into_iter().collect()
    }
}
fn main() {
    println!(
        "{:?}",
        Solution::four_sum(
            vec![1000000000, 1000000000, 1000000000, 1000000000],
            -1000000000
        )
    );
}
