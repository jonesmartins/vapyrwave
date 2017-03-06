# Vapyrwave

This program turns your cool sentences into ＶＡＰＯＲＷＡＶＥ sentences with fullwidth characters.

Requires Pyperclip and Argparse

### Installation

 - Clone or download the file.
 - Install Pyperclip and Argparse through Pip.
 - See instructions for more.

### Usage:
```sh
py vaporwave.py [-v] [-s SPACES] [sentence between quotes]
``` 
The optional -v flag verticalizes your sentence.
The optional -s flags adds N spaces between your characters
  
### Example:
```sh
$ py vaporwave.py "it works!" -s 1
$ Result in your clipboard.

Clipboard: ｉ ｔ   ｗ ｏ ｒ ｋ ｓ ！
```
And also:
```sh
$ py vaporwave.py "Verticalized!" -v
$ Result in your clipboard.

Clipboard: Ｖ
           ｅ
           ｒ
           ｔ
           ｉ
           ｃ
           ａ
           ｌ
           ｉ
           ｚ
           ｅ
           ｄ
           ！
```
Or maybe:
```sh
$ py vaporwave.py "aesthetics!" -v -s 1
$ Result in your clipboard.

Clipboard: ａ ｅ ｓ ｔ ｈ ｅ ｔ ｉ ｃ ｓ 
           ｅ
           ｓ
           ｔ
           ｈ
           ｅ
           ｔ
           ｉ
           ｃ
           ｓ
```
