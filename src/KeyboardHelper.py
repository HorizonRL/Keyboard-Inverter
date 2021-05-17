from enum import Enum

import win32clipboard as clipboard
from pynput.keyboard import Key, Controller
import time


class CtrlKeys(Enum):
    ALL = "a"
    COPY = "c"
    PASTE = "v"


keyboard = Controller()


def keyboard_ctrl_press(key: CtrlKeys):
    keyboard.press(Key.ctrl)
    keyboard.press(key.value)

    keyboard.release(key.value)
    keyboard.release(Key.ctrl)


def unfocused_tab():
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)

    keyboard.release(Key.alt)
    keyboard.release(Key.tab)


def put_clipboard(text: str):
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(clipboard.CF_UNICODETEXT, text)
    clipboard.CloseClipboard()


def read_clipboard(clean=False):
    clipboard.OpenClipboard()
    try:
        data = clipboard.GetClipboardData(clipboard.CF_UNICODETEXT)
    except TypeError:
        data = ""
    if clean:
        clipboard.EmptyClipboard()
    clipboard.CloseClipboard()
    return data


def read_for_invert(is_all: bool) -> str:
    if is_all:
        keyboard_ctrl_press(CtrlKeys.ALL)

    keyboard_ctrl_press(CtrlKeys.COPY)
    time.sleep(0.1)

    return read_clipboard()


def put_inversion(text: str):
    put_clipboard(text)
    keyboard_ctrl_press(CtrlKeys.PASTE)
