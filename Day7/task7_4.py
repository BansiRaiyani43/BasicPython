# Write a program to read json file and show in terminal.
# Write a program to dump/write data in json file.

import json
x = {
    "name" : "Jhon David",
    "age" : "28",
    "city" : "London"
}
y = json.dumps(x, indent=6)
print(y)