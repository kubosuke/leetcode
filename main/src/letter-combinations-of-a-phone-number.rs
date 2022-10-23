// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

struct Solution {}

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        let mut res: Vec<String> = vec![];

        if digits.len() == 0 {
            return res;
        }

        let m: std::collections::HashMap<char, &str> = [
            ('1', ""),
            ('2', "abc"),
            ('3', "def"),
            ('4', "ghi"),
            ('5', "jkl"),
            ('6', "mno"),
            ('7', "pqrs"),
            ('8', "tuv"),
            ('9', "wxyz"),
        ]
        .iter()
        .cloned()
        .collect();

        for c in digits.chars() {
            let letters = m.get(&c).unwrap();
            let mut tmp: Vec<String> = vec![];

            for cc in letters.chars() {
                if res.len() == 0 {
                    tmp.push(cc.to_string());
                } else {
                    for r in res.iter() {
                        tmp.push(r.to_owned() + &cc.to_string());
                    }
                }
            }
            res = tmp;
        }
        res
    }
}
fn main() {}
