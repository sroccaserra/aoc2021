use std::env::args;
use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn get_parsed_lines<T>(parse: fn(String) -> T) -> Vec<T> {
    let filename = args().nth(1).unwrap();
    let file = File::open(filename).unwrap();

    BufReader::new(file)
        .lines()
        .map(Result::unwrap)
        .map(parse)
        .collect()
}
