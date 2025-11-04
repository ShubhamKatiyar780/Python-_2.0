file_path = 'C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/samplefile.txt'


# Error Handling
# ============================
try:
    with open(file_path, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"An error occurred: {e}")

