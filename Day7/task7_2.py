#Create a function that returns the selected filename from a path. Include the extension in your answer.

import os

def get_filename_from_path(path):
    return os.path.basename(path)

print(get_filename_from_path("/document/basicpython/day2/task2_2.py"))  
