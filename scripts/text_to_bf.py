#!/usr/bin/python3
import sys

current_specials  = ord(" ")
current_uppercase = ord("A")
current_lowercase = ord("a")

# TODO: Make the program automatically change to a new character set, like specials, upper or lowercase.
current_position = 1

# 0 newline, 1 specials, 2 uppercase, 3 lowercase
output_string = "***writing to output***\n"

def compare_to_currents(value: int, current: int):
    if value > current:
        return (("+" * (value - current)) + f". {value}\n")
    elif value < current:
        return ("-" * (current - value) + f". {value}\n")
    else:
        return f". {value}\n"

if len(sys.argv) >= 2:
    argument = sys.argv[1]

    # for each character in the string...
    for c in argument:

        # check if it's uppercase, lowercase, or special
        tmp = ord(c)

        if c.isupper():
            output_string += compare_to_currents(tmp, current_uppercase)
            current_uppercase = tmp

        elif c.islower():
            output_string += compare_to_currents(tmp, current_lowercase)
            current_lowercase = tmp
            
        elif (tmp >= 32) or (tmp <= 64):
            output_string += compare_to_currents(tmp, current_specials)
            current_specials = tmp

print(output_string)
