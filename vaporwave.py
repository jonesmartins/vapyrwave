import pyperclip
import sys

"""
Using a dictionary is not very efficient, but is predictable.
"""
def vaporwave(sentence):
    character_dict = {"!": "！", "#": "＃", "$": "＄", "%": "％", "&": "＆", "'": "＇", "(": "（",
                  ")": "）", "*": "＊", "+": "＋", ",": "，", "-": "－", ".": "．", "/": "／",
                  "0": "０", "1": "１", "2": "２", "3": "３", "4": "４", "5": "５", "6": "６",
                  "7": "７", "8": "８", "9": "９", ":": "：", ";": "；", "<": "＜", "=": "＝",
                  ">": "＞", "?": "？", "@": "＠", "A": "Ａ", "B": "Ｂ", "C": "Ｃ", "D": "Ｄ",
                  "E": "Ｅ", "F": "Ｆ", "G": "Ｇ", "H": "Ｈ", "I": "Ｉ", "J": "Ｊ", "K": "Ｋ",
                  "L": "Ｌ", "M": "Ｍ", "N": "Ｎ", "O": "Ｏ", "P": "Ｐ", "Q": "Ｑ", "R": "Ｒ",
                  "S": "Ｓ", "T": "Ｔ", "U": "Ｕ", "V": "Ｖ", "W": "Ｗ", "X": "Ｘ", "Y": "Ｙ",
                  "Z": "Ｚ", "[": "［","\\": "＼", "]": "］", "^": "＾", "_": "＿", "`": "｀",
                  "a": "ａ", "b": "ｂ", "c": "ｃ", "d": "ｄ", "e": "ｅ", "f": "ｆ", "g": "ｇ",
                  "h": "ｈ", "i": "ｉ", "j": "ｊ", "k": "ｋ", "l": "ｌ", "m": "ｍ", "n": "ｎ",
                  "o": "ｏ", "p": "ｐ", "q": "ｑ", "r": "ｒ", "s": "ｓ", "t": "ｔ", "u": "ｕ",
                  "v": "ｖ", "w": "ｗ", "x": "ｘ", "y": "ｙ", "z": "ｚ", "{": "｛", "|": "｜",
                  "}": "｝", "~": "～"}
    new_sentence = ""
    for character in sentence:
        if character in character_dict:
            new_sentence += character_dict[character] + " "
        else:
            new_sentence += character + " "

    pyperclip.copy(new_sentence)
    print("Result in your clipboard.")


def parse_cmd(text):
    if text[:6] == "upper ":
        vaporwave(text[6:].upper())
    elif text[:6] == "lower ":
        vaporwave(text[6:].lower())
    elif text[:8] == "capital ":
        vaporwave(text[8:].capitalize())
    elif text == "":
        print("Exiting.")
        sys.exit() #breaks while loop
    else:
        print("Input Error.")


def main(argv):
    length = len(argv)
    if length == 1:
        while True:
            sentence = input("Sentence: ")
            parse_cmd(sentence)
    elif length == 3:
        sentence = "{} {}".format(sys.argv[1], sys.argv[2])
        parse_cmd(sentence)
    else:
        print("Command Error.")

main(sys.argv)
