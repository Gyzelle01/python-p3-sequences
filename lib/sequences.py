#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacc_sequence = []

    if length == 0:
        fibonacc_sequence = []
    
    elif length == 1:
        fibonacc_sequence = [0]

    elif length == 2:
        fibonacc_sequence = [0, 1]

    else:
        fibonacc_sequence = [0, 1]
        for i in range(2, length):
            fibonacc_sequence.append(fibonacc_sequence[i - 1] + fibonacc_sequence[i - 2])

   
    print(fibonacc_sequence)