def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]

    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

def main():
    try:
        n = int(input("Enter the number of terms for the Fibonacci sequence: "))
        if n < 0:
            print("Please enter a positive integer.")
            return

        
        fibonacci_sequence = generate_fibonacci(n)
        print(f"Fibonacci sequence up to {n} terms: {fibonacci_sequence}")

    except ValueError:
        print("Invalid input. Please enter an integer.")

main()
