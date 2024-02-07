fn main() {
    let mut fib_sequence = vec![0, 1];
    let mut last_number;
    let mut i = 2;
    loop {
        last_number = fib_sequence[i-1] + fib_sequence[i-2];
        if last_number > 4000000 {
            break;
        }
        fib_sequence.push(last_number);
        i += 1;
    }
    let sum: i32 = fib_sequence.iter().filter(|&x| x % 2 == 0).sum();
    println!("{}", sum);
}