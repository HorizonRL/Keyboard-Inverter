from enum import Enum

import win32clipboard
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


def read_clipboard(is_all: bool) -> str:
    if is_all:
        keyboard_ctrl_press(CtrlKeys.ALL)
    keyboard_ctrl_press(CtrlKeys.COPY)
    time.sleep(0.05)

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data


def put_clipboard(text: str):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text)
    win32clipboard.CloseClipboard()

    keyboard_ctrl_press(CtrlKeys.PASTE)
