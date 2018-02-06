import sys

import argparse
import pyperclip


def read_argv(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('sentence', help='Sentence to transform')
    parser.add_argument('-v', dest='vertical', action='store_true',
                        help='Prints result in vertical manner')
    parser.add_argument('-s', dest='spaced', default=1, type=int,
                        help='Prints result with spaces amidst letters')
    return parser.parse_args(argv)


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
    new_sentence = '\n'.join([s for s in sentence])
    return new_sentence.rstrip('\n')


def make_horizontal(sentence, spaces):
    spaces_str = ' ' * spaces
    new_sentence = spaces_str.join([s for s in sentence])
    return new_sentence


def make_both(sentence, spaces):
    final_sentence = '{}\n'.format(make_horizontal(sentence, spaces))
    vertical = '\n'.join(sentence[1:])
    return final_sentence + vertical


def send_to_clipboard(sentence):
    pyperclip.copy(sentence)
    print("Saved on your clipboard.")

    
def main(argv):
    cmd = vars(read_argv(argv))
    sentence = transform_vaporwave(cmd['sentence'])
    if cmd['vertical'] and cmd['spaced']:
        sentence = make_both(sentence, cmd['spaced'])
    elif cmd['spaced']:
        sentence = make_horizontal(sentence, cmd['spaced'])
    elif cmd['vertical']:
        sentence = make_vertical(sentence)
    
    send_to_clipboard(sentence)

    
if __name__ == '__main__':
    main(sys.argv[1:])
