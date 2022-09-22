#[path = "common/common.rs"]
mod common;

use common::get_parsed_lines;

fn solve(commands: &Vec<Command>) -> (i32, i32) {
    let (mut hpos, mut depth_1, mut depth_2, mut aim) = (0, 0, 0, 0);
    for command in commands {
        match command.direction.as_str() {
            "forward" => {
                hpos += command.value;
                depth_2 += aim * command.value;
            }
            "up" => {
                depth_1 -= command.value;
                aim -= command.value;
            }
            "down" => {
                depth_1 += command.value;
                aim += command.value;
            }
            _ => panic!(),
        }
    }
    (hpos * depth_1, hpos * depth_2)
}

struct Command {
    direction: String,
    value: i32,
}

fn parse(line: String) -> Command {
    let chunks: Vec<_> = line.split_whitespace().collect();
    let direction = chunks[0].to_string();
    let value = chunks[1].parse().unwrap();

    Command{ direction, value }
}

fn main() {
    let commands = get_parsed_lines(parse);
    let (result_1, result_2) = solve(&commands);
    println!("{result_1}\n{result_2}");
}
