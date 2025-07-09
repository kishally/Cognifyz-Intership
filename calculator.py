#Task 4: Calculator Program
'''Create a Python program that acts as a basic calculator. It should prompt the user to 
enter two numbers and an operator (+,-,*,/,%), and then display the result of the operation.'''

def calculator():
    num = input("enter the input:").split()
    
    try:
        if len(num) != 3:
            raise ValueError()
        
        try:
            a = float(num[0])
            b = float(num[1])
            op = num[2]
        except ValueError:
            raise ValueError()
        
        if (op == "+"):
            result = a + b
        elif (op == "-"):
            result = a - b
        elif (op == "*"):
            result = a * b
        elif (op == "/"):
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = a / b
        elif (op == "%"):
            if b == 0:
                raise ZeroDivisionError("Cannot module by zero.")
            result = a % b
        else:
            raise ValueError()
        
        if result == int(result):
            result = int(result)

        print(result)
    except ValueError:
        print("Input must be in the format: num num operator (e.g., 1 2 +)")
    except ZeroDivisionError as ze:
        print(f"Math Error: {ze}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

calculator()