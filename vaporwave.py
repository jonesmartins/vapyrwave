import sys, pyperclip

def transform_vaporwave(sentence):
    new_sentence = ""
    for character in sentence:
        ord_char = ord(character)
        if ord_char >= 33 and ord_char <= 127:
            new_sentence += chr(ord_char + 65248) + " "    
        else:
            new_sentence += character + " "

    pyperclip.copy(new_sentence)  # sends result to clipboard
    print("Result in your clipboard.")

def parse_cmd(text):
    command = text[:6].lower() 
    if command == "upper ":
        string = text[6:].upper()
    elif command == "lower ":
        string = text[6:].lower()
    elif command == "title ":
        string = text[6:].title()
    elif text == "":
        sys.exit("Exiting.")  # stops while loop
    else:
        sys.exit("Input Error.")  # stops program
        
    transform_vaporwave(string)
    

def main(argv):
    if len(argv) == 1:  # only filename
        while True:
            sentence = input("Sentence: ")
            parse_cmd(sentence)
    else:
        sentence = " ".join(argv[1:])
        parse_cmd(sentence)    
    
if __name__ == '__main__':
    main(sys.argv)

