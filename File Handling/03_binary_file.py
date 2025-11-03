# Working with Binary Files
# ============================
# Reading binary file (like images)
with open("C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/college_group_pic.jpg", "rb") as file:
    binary_data = file.read()
# Writing binary file
with open("C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/copy.jpg", "wb") as file:
    file.write(binary_data)
# or
with open("C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/college_group_pic.jpg", "rb") as f1:
    with open("C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/college_group_pic_copy.jpg", "wb") as f2:
        f2.write(f1.read())
