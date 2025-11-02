import os

file_path = 'C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/samplefile.txt'


# Check if file exists
if os.path.exists(file_path):
    print("File exists!")
else:
    print("File not exists!")


# Get file size
size = os.path.getsize(file_path)
print(size)

# Get absolute path
abs_path = os.path.abspath(file_path)
print(abs_path)


