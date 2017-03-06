import pyperclip
import argparse
import sys

def read_argv(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('sentence', help='Sentence to transform')
    parser.add_argument('-v', dest='vertical', action='store_true',
                        help='Prints result in vertical manner')  
    parser.add_argument('-s', dest='spaced', default=0, type=int,
                        help='Prints result with N spaces amidst letters')
    return parser.parse_args(argv)


def check_cmd(cmd):
    try:
        return vars(cmd)
    except TypeError:
        return cmd


def transform_vaporwave(sentence):
    new_sentence = ''
    char_distance = ord('Ａ') - ord('A')  # 65248
    for character in sentence:
        ord_char = ord(character)
        if ord('!') <= ord_char <= ord('~'):
            character = chr(ord_char + char_distance)
        new_sentence += character
    return new_sentence


def make_vertical(sentence):
    new_sentence = ''
    for letter in sentence:
        new_sentence += '{}\n'.format(letter)
    return new_sentence.rstrip('\n')


def make_horizontal(sentence, spaces):
    new_sentence = ''
    for letter in sentence:
        new_sentence += '{}{}'.format(letter, ' '*spaces)
    return new_sentence


def make_both(sentence, spaces):
    final_sentence = '{}\n'.format(make_horizontal(sentence, spaces))
    for pos in range(1, len(sentence)):
        final_sentence += '{}\n'.format(sentence[pos])
    return final_sentence.rstrip('\n')

   
def send_to_clipboard(sentence):
    pyperclip.copy(sentence)
    print("Result in your clipboard.")

    
def main(argv):
    cmd = read_argv(argv)
    cmd_dict = check_cmd(cmd)    
    sentence = transform_vaporwave(cmd_dict['sentence'])
    if cmd_dict['vertical'] and cmd_dict['spaced']:
        sentence = make_both(sentence, cmd_dict['spaced'])
    elif cmd_dict['spaced']:
        sentence = make_horizontal(sentence, cmd_dict['spaced'])
    elif cmd_dict['vertical']:
        sentence = make_vertical(sentence)
    
    send_to_clipboard(sentence)
    
if __name__ == '__main__':
    main(sys.argv[1:])
