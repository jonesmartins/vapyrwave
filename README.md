# Vapyrwave

This program turns your cool sentences into even cooler ＶＡＰＯＲＷＡＶＥ sentences with [fullwidth characters](https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms).

Requires `pyperclip` and `argparse`.

### Installation

 - Download the `vapyrwave.py` or clone the project.
 - Manually install `pyperclip` and `argparse` through `pip` or run `pip install -r requirements.txt` with this project's requirements file.
 - You're set!

Notes from Pyperclip's documentation (2020-06-03):

```
Currently only handles plaintext.

On Windows, no additional modules are needed.

On Mac, this module makes use of the pbcopy and pbpaste commands, which should come with the os.

On Linux, this module makes use of the xclip or xsel commands, which should come with the os. 

Otherwise run “sudo apt-get install xclip” or “sudo apt-get install xsel” (Note: xsel does not always seem to work.)

Otherwise on Linux, you will need the gtk or PyQt4 modules installed.
```

### Usage

```sh
python vapyrwave.py [-h] [-s SPACES | -v | -b [BOTH]] sentence
``` 

The optional -v/--vertical flag verticalizes your sentence.
The optional -s/--spaces flag adds N spaces between characters.
The optional -b/--both flag joins vertical and horizontal results and adds N spaces between characters.

### Examples

## No flags

```sh
$ py vapyrwave.py "No flags"
>>> Ｎｏ ｆｌａｇｓ
>>> Result saved to clipboard.
```

## With spaces

```sh
$ py vapyrwave.py "Spaced characters" -s  2
>>> Ｓ  ｐ  ａ  ｃ  ｅ  ｄ     ｃ  ｈ  ａ  ｒ  ａ  ｃ  ｔ  ｅ  ｒ  ｓ
>>> Result saved to clipboard.
```

## Verticalized

```sh
$ py vapyrwave.py "Verticalized" -v
>>> Ｖ
>>> ｅ
>>> ｒ
>>> ｔ
>>> ｉ
>>> ｃ
>>> ａ
>>> ｌ
>>> ｉ
>>> ｚ
>>> ｅ
>>> ｄ
>>> Result saved to clipboard.
```

## Both

```sh
$ py vapyrwave.py "Why not both?" -b 1
>>> Ｗ ｈ ｙ   ｎ ｏ ｔ   ｂ ｏ ｔ ｈ ？
>>> ｈ
>>> ｙ
>>>  
>>> ｎ
>>> ｏ
>>> ｔ
>>>  
>>> ｂ
>>> ｏ
>>> ｔ
>>> ｈ
>>> ？
>>> Result saved to clipboard.
```
