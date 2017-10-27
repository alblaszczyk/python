import sys

keyboard_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
keyboard_dict = {}

def build_dictionary():
    for index, char in enumerate(keyboard_list):
        for c in char:
            keyboard_dict[c] = index + 2
    return keyboard_dict

def translate_my_number(numbers):
    build_dictionary()
    digits = ''
    for item in numbers:
        if item.isdigit() or item == "-":
            digits = digits + str(item)
        else:
            for key in keyboard_dict:
                if item == key in keyboard_dict:
                    digits = digits + str(keyboard_dict[key])
    return digits
print(translate_my_number(sys.argv[1]))
