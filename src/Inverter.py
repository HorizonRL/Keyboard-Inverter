import sys
import time

import KeyboardHelper
import LangsDictionary


def to_heb(s: str) -> str:
    converted = ""
    for c in s:
        try:
            converted += LangsDictionary.HEB_ENG_QWERTY[c.capitalize()]

        except KeyError:
            converted += c
    return converted


def to_eng(s: str) -> str:
    key_list = list(LangsDictionary.HEB_ENG_QWERTY.keys())
    val_list = list(LangsDictionary.HEB_ENG_QWERTY.values())

    converted = ""
    for c in s:
        if c in val_list:
            pos = val_list.index(c)
            converted += key_list[pos]
        else:
            converted += c

    return converted.lower()


def is_eng(s: str) -> bool:
    key_list = list(LangsDictionary.HEB_ENG_QWERTY.keys())
    eng_counter = 0

    for c in s:
        if c.capitalize() in key_list:
            eng_counter += 1

    return len(s) - eng_counter < eng_counter


if __name__ == '__main__':
    is_all = int(sys.argv[1]) == 1
    time.sleep(1.5 if is_all else 3)
    t = KeyboardHelper.read_clipboard(is_all)
    conv = ""

    if is_eng(t):
        conv = to_heb(t)
    else:
        conv = to_eng(t)

    KeyboardHelper.put_clipboard(conv)
