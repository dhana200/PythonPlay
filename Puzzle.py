import os
import re

# Define a function to search for a phone number pattern in a file
def search_number(filepath, pattern):
    with open(filepath, 'r') as file:
        content = file.read()
        match = re.search(pattern, content)
        if match:
            print("Phone number found:", match.group())
            print("Phone number found in file:", filepath)

# Get the current working directory
current_dir = os.getcwd()

# Compile the regular expression pattern for phone numbers (format: xxx-xxx-xxxx)
phno_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

flag = False

# Walk through all folders and files in the current directory
for folders, subfolders, files in os.walk(current_dir):
    for filename in files:
        # Check if the file has a .txt extension
        if filename.endswith('.txt'):
            # Build the full path to the file
            current_file_path = os.path.join(folders, filename)
            # Search for the phone number pattern in the file
            search_number(current_file_path, phno_pattern)