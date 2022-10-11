// https://leetcode.com/problems/longest-palindromic-substring/

use proconio::input;

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

struct Solution;

impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let c: Vec<char> = s.chars().collect();
        let n = s.len();

        // edge
        if n == 1 {
            return c[0].to_string()
        } else if n == 2 {
            if c[0] == c[1] {
                return s;
            } else {
                return c[0].to_string();
            };
        }

        let mut ans = c[0].to_string();
        let mut ans_c = 1;
        for i in 0..n {
            // odd
            let mut l = i as isize - 1;
            let mut r = i as isize + 1;
            loop {
                if l < 0 || n <= r as usize {
                    break;
                }
                if c[l as usize] == c[r as usize] {
                    if chmax!(ans_c, (r-l+1) as usize) {
                        ans = c[l as usize..=r as usize].iter().collect::<String>();
                    }
                    l -= 1;
                    r += 1;
                } else {
                    break;
                }               
            }

            // even
            let mut l = i as isize;
            let mut r = i as isize + 1;
            loop {
                if l < 0 || n <= r as usize {
                    break;
                }
                if c[l as usize] == c[r as usize] {
                    if chmax!(ans_c, (r-l+1) as usize) {
                        ans = c[l as usize..=r as usize].iter().collect::<String>();
                    }
                    l -= 1;
                    r += 1;
                } else {
                    break;
                }          
            }
        }   
        ans
    }
}

fn main() {
    input! {
        st: String
    }
    println!("{}", Solution::longest_palindrome(st));
}
