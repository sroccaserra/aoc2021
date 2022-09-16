#[path = "common/common.rs"] mod common;

const HUGE: i32 = 9999999;

fn solve_1(numbers: Vec<i32>) -> i32 {
    let mut previous = HUGE;
    let mut result = 0;
    for n in numbers {
        if n > previous {
            result += 1;
        }
        previous = n;
    }
    return result;
}

fn main() {
    let numbers = common::get_parsed_lines(|s| s.parse::<i32>().unwrap());
    println!("{}", solve_1(numbers));
}
