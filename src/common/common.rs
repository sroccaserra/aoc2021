use std::env;
use std::fs::File;
use std::io::{self, BufRead};

pub fn get_parsed_lines<T, F: Fn(String) -> T>(parse: F) -> Vec<T> {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    let file = File::open(filename).unwrap();
    return io::BufReader::new(file)
        .lines()
        .map(|x| parse(x.unwrap()))
        .collect::<Vec<T>>();
}

