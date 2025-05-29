#Create a Program that creates product IDs for different fruit juices.
"""
Example :
	("apple", "500ml") ➞ "APP500"

	("pineapple", "45ml") ➞ "PIN45"

	("passion fruit", "750ml") ➞ "PASFRU750"
"""

def format_tuple(data):
    fruit, volume = data
    fruit_part = fruit[:3].upper()
    volume_part = ''.join(filter(str.isdigit, volume))
    return fruit_part + volume_part

result = format_tuple(("pineapple","45ml"))
result1 = format_tuple(("apple","500ml"))
print(result)
print(result1)