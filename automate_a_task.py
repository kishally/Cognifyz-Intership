# Task 3: Automate a Task
'''Identify a repetitive task, such as data processing, file management, 
or report generation, and develop a script to automate it using Python. 
This task will showcase their problem-solving skills and familiarity with 
Python's automation capabilities.'''

import os
import shutil

def organize_files_by_type(directory):
    try:
        if not os.path.isdir(directory):
            print("Provided path is not a valid directory.")
            return

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            if os.path.isfile(file_path):
                ext = filename.split('.')[-1].lower()

                if '.' not in filename:
                    continue

                folder_name = ext + "_files"
                folder_path = os.path.join(directory, folder_name)

                os.makedirs(folder_path, exist_ok=True)

                shutil.move(file_path, os.path.join(folder_path, filename))

        print("Files organized successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_folder = input("Enter the path to the folder you want to organize: ").strip()
    organize_files_by_type(target_folder)
