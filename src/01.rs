#[path = "common/common.rs"]
mod common;

use common::get_parsed_lines;

const HUGE: i32 = 9999999;

fn solve_1(numbers: &Vec<i32>) -> i32 {
    let mut previous = HUGE;
    let mut result = 0;
    for &n in numbers {
        if n > previous {
            result += 1;
        }
        previous = n;
    }
    result
}

fn solve_2(numbers: &Vec<i32>) -> i32 {
    let (mut p_1, mut p_2, mut p_3) = (HUGE, HUGE, HUGE);
    let mut result = 0;
    for &n in numbers {
        if n + p_1 + p_2 > p_1 + p_2 + p_3 {
            result += 1;
        }
        (p_1, p_2, p_3) = (n, p_1, p_2);
    }
    result
}

fn main() {
    let numbers = get_parsed_lines(|s| s.parse().unwrap());
    println!("{}", solve_1(&numbers));
    println!("{}", solve_2(&numbers));
}
