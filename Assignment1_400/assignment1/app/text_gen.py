import os
import random
import string

# Define the directory path
dir_path = '/serverdata'

# Create the directory if it doesn't exist
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Define the file path
file_path = os.path.join(dir_path, 'random.txt')

# Check if the file exists
if file_path:
    # Read and print existing content
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            print("Existing content:")
            print(file.read())

# Generate random text data
random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=100))

# Write new data to the file
with open(file_path, 'w') as file:
    file.write(random_text)

# Print the new data
print("New content:", random_text)