# Write a program to read json file and show in terminal.
# Write a program to dump/write data in json file.

import json
x = {
"name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y = json.dumps(x, indent=6)
print(y)