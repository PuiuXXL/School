def generate_String(string):
    new_string = ""
    for char in string:
        new_string += (chr(ord(char) + 1))
    return new_string


string = "abc"
print(generate_String(string))