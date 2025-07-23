#Task 5: File Manipulation
'''Write a Python program that reads a text  file and counts the occurrences of each word 
in the file. Display the results in alphabetical order along with their respective counts.'''

def count_words_in_file(filename):
    try:
        # open and read the file
        with open(filename, 'r') as file:
            text = file.read()

        # Clean and normalize text
        words = text.lower().split()
        
        word_counts = {}

        # Remove punctuation from each word
        for word in words:
            word = ''.join(char for char in word if char.isalnum())
            if word:
                word_counts[word] = word_counts.get(word, 0) + 1

        # Display sorted results
        print("Word Frequencies (A-Z):")
        for word in sorted(word_counts):
            print(f"{word}: {word_counts[word]}")

    except FileNotFoundError:
        print("File not found. Please check the filename.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


filename = input("Enter the filename (e.g., sample.txt): ")
count_words_in_file(filename)
