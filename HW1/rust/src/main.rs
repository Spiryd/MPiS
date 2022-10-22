use std::io;
use rand::prelude::*;
use rand_pcg::Pcg64;

fn main() {
    let rng: Pcg64 = Pcg64::from_entropy();


    
    loop {
        
        println!("-+++- MENU -+++-\n1. one\n0. exit");
        println!("Your choice: ");

        let mut choice = String::new();

        io::stdin()
            .read_line(&mut choice)
            .expect("Failed to read line");

        let choice: u8 = choice.trim().parse().expect("something went wrong");

        match choice{
            1=>println!("one"),
            0=>break,
            _=>println!("Try again!")
        }
    }
}
