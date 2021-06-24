import sys
import time

import KeyboardHelper
import LangsDictionary


def to_heb(s: str) -> str:
    converted = ""
    for c in s:
        try:
            converted += LangsDictionary.HEB_ENG_QWERTY[c.capitalize() if c.isalpha() else c]

        except KeyError:
            converted += c
    return converted


def to_eng(s: str) -> str:
    key_list = list(LangsDictionary.HEB_ENG_QWERTY.keys())
    val_list = list(LangsDictionary.HEB_ENG_QWERTY.values())

    converted = ""
    for c in s:
        try:
            pos = val_list.index(c)
            converted += key_list[pos]
        except ValueError:
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
    debug_mode = len(sys.argv) <= 1
    if debug_mode:
        is_all = True
    else:
        is_all = int(sys.argv[1]) == 1

    clipboard_data = KeyboardHelper.read_clipboard(clean=True)

    KeyboardHelper.unfocused_tab()
    time.sleep(0.3 if is_all else 0.7)
    t = KeyboardHelper.read_for_invert(is_all)
    is_from_caps = t.isupper()

    if is_eng(t):
        conv = to_heb(t)
    else:
        conv = to_eng(t)
    KeyboardHelper.put_inversion(conv)
    KeyboardHelper.change_comp_lang()

    time.sleep(0.05)
    if is_from_caps:
        KeyboardHelper.toggle_caps()
    else:
        KeyboardHelper.put_clipboard(clipboard_data)

