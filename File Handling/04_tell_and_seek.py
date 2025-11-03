file_path = 'C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/samplefile.txt'

# tell() and seek()
# ============================
with open(file_path, "r") as file:
    # Check if file is readable/writable
    print(file.readable())    # True
    print(file.writable())    # False (in 'r' mode)
    file.read(3)
    # Get current position
    position = file.tell()
    print(position) # 3
    # Change file position
    a=file.seek(7)  # cursor go to 7th position
    print(a)
    print(file.read()) # read characters from the 7th position


# seek() during the 'write' mode
with open(file_path, "w") as file:
    file.write("Shubham")
    file.seek(0)
    file.write("La") # Labham