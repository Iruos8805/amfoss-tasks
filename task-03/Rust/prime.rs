use std::io;

fn is_prime(num: u32) -> bool {
    if num <= 1 {
        return false;
    }
    for i in 2..num {
        if num % i == 0 {
            return false;
        }
    }
    true
}

fn main() {
    let mut input = String::new();
    println!("Enter a number: ");
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: u32 = input.trim().parse().expect("Invalid input");
    
    println!("Prime numbers up to {}:", n);
    for num in 2..=n {
        if is_prime(num) {
            println!("{}", num);
        }
    }
}
