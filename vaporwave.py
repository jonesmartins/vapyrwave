import pyperclip
import sys
import argparse

def read_argv(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('sentence', type=str, help='Sentence to transform')
    parser.add_argument('-v', '--vertical', dest='vertical', action='store_true',
                        help='Prints result in vertical and horizontal manner')
    return parser.parse_args(argv)

def check_cmd(cmd):
    try:
        return vars(cmd)
    except TypeError:
        return cmd

def transform_vaporwave(sentence):
    new_sentence = ""
    for character in sentence:
        ord_char = ord(character)
        if 33 <= ord_char <= 127:
            character = chr(ord_char + 65248)
        new_sentence += character + " "
    return new_sentence.rstrip()

def add_vertical(sentence):
    final_sentence = "{}\n".format(sentence)
    for pos in range(2, len(sentence), 2):
        final_sentence += "{}\n".format(sentence[pos])
    return final_sentence.rstrip('\n')

def send_to_clipboard(sentence):
    pyperclip.copy(sentence)  # remove last space
    print("Result in your clipboard.")
    
'''
def parse_cmd(text):
    command = text[:6].lower()
    if command == "upper ":
        string = text[6:].upper()
    elif command == "lower ":
        string = text[6:].lower()
    elif command == "title ":
        string = text[6:].title()
    elif text == "":
        print("Exiting.")
        sys.exit() #stops while loop
    else:
        print("Input Error.")
        sys.exit() #stops program

    transform_vaporwave(string)
'''

def main():
    cmd = read_argv(sys.argv[1:])
    cmd_dict = check_cmd(cmd)
    sentence = transform_vaporwave(cmd_dict['sentence'])
    if cmd_dict['vertical']:
        sentence = add_vertical(sentence)
    send_to_clipboard(sentence)

if __name__ == '__main__':
    main()
