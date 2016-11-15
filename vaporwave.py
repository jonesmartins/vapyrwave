import pyperclip
import sys

def transform_vaporwave(sentence):
    new_sentence = ""
    for character in sentence:
        ord_char = ord(character)
        if ord_char >= 33 and ord_char <= 127:
            new_sentence += chr(ord_char + 65248) + " "
        else:
            new_sentence += character + " "
            
    pyperclip.copy(new_sentence)
    print("Result in your clipboard.")


def parse_command(text):
    command = text[:6]
    string = text[6:]
    if command == "upper ":
        string = string.upper()
    elif command == "lower ":
        string = string.lower()
    elif command == "title ":
        string = string.title()
    elif text == "":
        print("Exiting.")
        sys.exit() #breaks while loop
    else:
        print("Input Error.")
        sys.exit() #stops program
        
    transform_vaporwave(string) 

def main(argv):
    length = len(argv)
    if length == 1:
        while True:
            sentence = input("Sentence: ")
            parse_command(sentence)
    elif length == 3:
        sentence = "{} {}".format(sys.argv[1], sys.argv[2])
        parse_command(sentence)
    else:
        print("Command Error.")

main(sys.argv)
