# Deserialization ---> Process of converting JSON fromat to  python data types.

import json


file_path = 'C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/samplefile.json'


# Use json.load() for reading directly from file objects
# Use json.loads() when you have JSON data as a string
with open(file_path, 'r') as f:
    data1 = json.load(f)


print(data1)
print(type(data1))


print(data1['user_info']['name'])