# Serialization ---> Process of converting python data types to JSON fromat.

import json

file_path = 'C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/samplefile.json'

# Combine both data structures
data = {
    'items': [1, 2, 3, 4, 5, 6],
    'user_info': {
        'name': 'Shubham',
        'age': 24,
        'state': 'UP'
    }
}

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)