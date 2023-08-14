def fibonacci_series(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


if __name__ == "__main__":
    first_50_fibonacci = fibonacci_series(50)
    sum_fibonacci = sum(first_50_fibonacci)

    print("First 50 Fibonacci numbers:")
    print(first_50_fibonacci)

    print(f"Sum of the first 50 Fibonacci numbers: {sum_fibonacci}")
