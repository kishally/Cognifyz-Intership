#Task 5: Palindrome Checker
'''Write a Python function that checks whethera given string is a palindrome. 
A palindrome is a word, phrase, or sequence that reads the same backward as forward 
(e.g., "madam" or "racecar")'''

def check_the_palindrome():
    input_word = input("enter the input:").lower()

    new_array = []
    for letter in input_word:
        if letter.isalnum():
            new_array.append(letter)
    new_word = "".join(new_array)

    if (new_word == new_word[::-1]):
        print("Palindrome")
    else:
        print("Not a Palindrome")

check_the_palindrome()
