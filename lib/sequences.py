#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print("[]")
    elif length == 1:
        print("[0]")
    else:
        fibonacci_seq = [0, 1]
        for i in range(2, length):
            next_num = fibonacci_seq[i - 1] + fibonacci_seq[i - 2]
            fibonacci_seq.append(next_num)

        fib_str = ', '.join(str(num) for num in fibonacci_seq)
        print("[" + fib_str + "]")

