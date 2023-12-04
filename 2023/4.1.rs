use std::fs::File;
use std::collections::HashSet;
use std::io::{BufReader, BufRead};

fn main() {
    let infile = File::open("4.in").unwrap();
    let reader = BufReader::new(infile);

    let mut total: u32 = 0;

    for line in reader.lines() {
        let line = line.unwrap();
        let skip = line.find(":").unwrap() + 1;
        let line = line[skip..].trim().to_string();
        let line = line.split("|").collect::<Vec<&str>>();
        let winning = line[0].trim().to_string();
        let mine = line[1].trim().to_string();
        let winning = winning
            .split(" ")
            .filter(|x| x != &"")
            .map(|x| x.parse::<u32>().unwrap())
            .collect::<HashSet<u32>>();
        let mut mine = mine
            .split(" ")
            .filter(|x| x != &"")
            .map(|x| x.parse::<u32>().unwrap())
            .collect::<Vec<u32>>();
        
        mine.retain(|x| winning.contains(x));
        
        let mut points: u32 = 0;

        if mine.len() > 0 {
            points = 1 << (mine.len() - 1);
        }

        total += points;
    }

    println!("{}", total);
}