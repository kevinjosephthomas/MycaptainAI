#fibonacci series
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        next_number = fib[i - 1] + fib[i - 2]
        fib.append(next_number)
    return fib

n = 30
fib_seq = fibonacci(n)
print(f"Fibonacci sequence up to {n} terms: {fib_seq}")
