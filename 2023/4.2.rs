use std::fs::File;
use std::collections::HashSet;
use std::io::{BufReader, BufRead};

fn main() {
    let infile = File::open("4.in").unwrap();
    let reader = BufReader::new(infile);

    let mut winnings: Vec<(usize, Vec<u32>)> = Vec::new();

    for (i, line) in reader.lines().enumerate() {
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
        
        winnings.push((i, mine));
        
    }

    let mut i = 0;
    while i < winnings.len() {
        let entry = &winnings[i];
        if entry.1.len() > 0 {
            for j in (entry.0 + 1)..(entry.0 + 1 + entry.1.len()) {
                winnings.push((j, winnings[j].1.clone()));
            }
        }
        i += 1;
    }

    println!("{}", winnings.len());
}