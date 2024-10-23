use std::io;

fn main() {
    let number = 5;
    println!("Guess: ");
    let mut guess = String::new();
    io::stdin().read_line(&mut guess).expect("Failed to read line");
    println!("You guessed: {}", guess);
    if guess.trim().parse::<i32>().unwrap() == number {
        println!("You guessed right!");
    } else {
        println!("You guessed wrong!");
    }
}
