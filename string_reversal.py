#Task 1: String Reversal
'''Create a Python function that takes a string as input and returns the reverse of that string. 
For example, if the input is"hello, " the function should return "olleh."'''

def revers_string():
    word = input("enter the input:") # input string is Hello
    res_str = word[::-1]
    print(res_str)

revers_string()