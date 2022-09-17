use std::env::{args};
use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn get_parsed_lines<T, F: Fn(String) -> T>(parse: F) -> Vec<T> {
    let filename = args().nth(1).unwrap();
    let file = File::open(filename).unwrap();

    return BufReader::new(file)
        .lines()
        .map(|x| parse(x.unwrap()))
        .collect();
}