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

def parse_cmd(text):
    command = text[:6].lower()  # just in case
    if command == "upper ":
        string = text[6:].upper()
    elif command == "lower ":
        string = text[6:].lower()
    elif command == "title ":
        string = text[6:].title()
    elif text == "":
        print("Exiting.")
        sys.exit()  # stops while loop
    else:
        print("Input Error.")
        sys.exit()  # stops program
        
    transform_vaporwave(string)
    

def main(argv):
    size_argv = len(argv)
    if size_argv == 1:  # Only filename
        while True:
            sentence = input("Sentence: ")
            parse_cmd(sentence)
    else:
        sentence = " ".join(argv[1:])
        parse_cmd(sentence)    
    

main(sys.argv)

