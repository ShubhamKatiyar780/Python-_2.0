file_path = 'C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/samplefile.txt'


# case 1- file open with 'WRITE' mode, create the file if it does not exist
with open(file_path, 'w') as f:
    f.write('Shubham Katiyar\n')
    f.write('Rajat Katiyar\n')


# The with statement automatically closes the file, even if an exception occurs
with open(file_path) as f:
    content = f.read()
    # print(content)
# File is automatically closed here


# case 2- if you write in existing file then remove the old all content and write the new content
with open(file_path, 'w') as f:
    f.write('Akshay Chauhan\n')

# case 3- file open with 'APPEND' mode, if you write in existing file without remove the old all content
with open(file_path, 'a') as f:
    f.write('Sameer Bhalla\n')

# case 4- write the multiple lines at one time
our_list = ['a\n', 'b\n', 'c\n', 'd\n', 'e\n']
with open(file_path, 'a') as f:
    f.writelines(our_list)


# case 5- file open with 'READ' (by default) mode, error if the file does not exist
file = open(file_path, 'r')
# Reads the entire file content as a single string
full_content = file.read()
# Reads one line at a time
single_line_at_a_time = file.readline()
# Reads all lines into a list of strings
all_lines_into_a_list = file.readlines()
# print(full_content)
# print(single_line_at_a_time)
# print(all_lines_into_a_list)
file.close()


# of you want to read entire data using readline()
with open(file_path, 'r') as f:
    line = f.readline()
    while line != '':
        # print(line, end="")
        line = f.readline()
# another logic
with open(file_path, 'r') as f:
    while True:
        line = f.readline()
        if line == '':
            break
        else:
            # print(line, end="")
            pass

# using read(10) method print only 10 character
with open(file_path, 'r') as f:
    # print(f.read(10)) # Approx 10 characters from entire content ---> ['Akshay Cha']
    # print(f.readline(10)) # Approx 10 characters from a line ---> ['uhan------']
    # print(f.readlines(10)) # Approx 10 bytes ---> ['Akshay Chauhan\n']
    pass
# ==================== Summary =====================================================================
# Function	   | Return Type |	Reads	              | Example Result
# ==================================================================================================
# read()	   |  String	 |  Entire file	          | 'Akshay Chauhan\nSameer Bhalla\n...'
# read(10)	   |  String	 |  10 chars	          | 'Akshay Cha'
# readline()   |  String	 |  1 line	              | 'Akshay Chauhan\n'
# readline(6)  |  String	 |  6 chars of first line | 'Akshay'
# readlines()  |  List	     |  All lines	          | ['Akshay Chauhan\n', 'Sameer Bhalla\n', ...]
# readlines(14)|  List	     |  Approx 14 bytes       | ['Akshay Chauhan\n']
# ==================== Summary =====================================================================

# with open(file_path) as f:
#   for x in f:
#     print(x, end='')


# Count lines and words in a file
# =================================
with open(file_path, "r") as file:
    lines = file.readlines()
    line_count = len(lines)
    word_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)
# print(f"Lines: {line_count}, Words: {word_count}")


# data loaded in chunks files
# ============================
with open(file_path, "r") as file:
    chunk_size = 2
    while len(file.read(chunk_size)) > 0:
        # print(file.read(chunk_size), end='*')
        file.read(chunk_size)
