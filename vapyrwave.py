import sys

import argparse
import pyperclip


def read_argv(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'sentence',
        help='Sentence to transform'
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-s', '--spaces',
        dest='spaces',
        type=int,
        help='Prints result with N spaces between characters'
    )

    group.add_argument(
        '-v', '--vertical',
        dest='vertical',
        action='store_true',
        help='Prints result vertically'
    )

    group.add_argument(
        '-b', '--both',
        dest='both',
        const=0,
        type=int,
        nargs='?',
        help='Prints result both vertically and horizontally with N spaces between characters'
    )

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
    new_sentence = '\n'.join(sentence)
    return new_sentence.rstrip('\n')


def add_spaces(sentence, spaces):
    spaces_str = ' ' * spaces
    new_sentence = spaces_str.join(sentence)
    return new_sentence


def make_both(sentence, spaces):
    horizontal = add_spaces(sentence, spaces) + '\n'
    vertical = '\n'.join(sentence[1:])
    return horizontal + vertical


def main(argv):
    cmd = read_argv(argv)

    fullwidth_sentence = transform_vaporwave(cmd.sentence)

    if cmd.spaces is not None:
        result = add_spaces(fullwidth_sentence, cmd.spaces)
    elif cmd.vertical:
        result = make_vertical(fullwidth_sentence)
    elif cmd.both is not None:
        result = make_both(fullwidth_sentence, cmd.both)
    else:
        result = fullwidth_sentence

    print(result)
    pyperclip.copy(result)
    print('Result saved to clipboard.')


if __name__ == '__main__':
    main(sys.argv[1:])
