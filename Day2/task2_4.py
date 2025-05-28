# Validate Pin
"""
A valid pin has:
	Exactly 4 or 6 characters.
	Only numerical characters (0-9).
	No whitespace.
"""
def valid_pin(pin):
    return(len(pin) == 4 or len(pin) == 6) and pin.isdigit()

print(valid_pin("123"))         #false
print(valid_pin("12345"))       #false
print(valid_pin("12gh3"))       #false
print(valid_pin("145623"))      #true