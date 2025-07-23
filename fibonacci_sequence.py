#Task 4: Fibonacci Sequence
'''Write a Python function that generates the Fibonacci sequence up to a given number of terms. 
The function should take an integer input from the user and display the Fibonacci sequence up to 
that number of terms'''

def generate_fibonacci(n_terms):
    if n_terms <= 0:
        print("Please enter a positive integer.")
        return

    fib_sequence = []

    a, b = 0, 1
    for i in range(n_terms):
        fib_sequence.append(a)
        a, b = b, a + b 

    result = " ".join(str(num) for num in fib_sequence)

    print(f"Fibonacci sequence: {result}")

try:
    user_input = int(input("Enter number of terms: "))
    generate_fibonacci(user_input)
except ValueError:
    print("Invalid input. Please enter an integer.")
