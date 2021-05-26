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


def change_comp_lang():
    keyboard.press(Key.alt)
    keyboard.press(Key.shift)

    keyboard.release(Key.alt)
    keyboard.release(Key.shift)


def open_clipboard():
    try:
        clipboard.OpenClipboard(0)
    except:
        pass


def close_clipboard():
    try:
        clipboard.CloseClipboard()
    except:
        pass


def put_clipboard(text: str):
    open_clipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(clipboard.CF_UNICODETEXT, text)
    close_clipboard()


def read_clipboard(clean=False):
    open_clipboard()
    try:
        data = clipboard.GetClipboardData()
    except TypeError:
        clipboard.EmptyClipboard()
        data = ""

    if clean:
        clipboard.EmptyClipboard()

    close_clipboard()
    return data


def read_for_invert(is_all: bool) -> str:
    if is_all:
        keyboard_ctrl_press(CtrlKeys.ALL)

    keyboard_ctrl_press(CtrlKeys.COPY)
    time.sleep(0.1)

    return read_clipboard()


def put_inversion(text: str):
    put_clipboard(text)
    time.sleep(0.1)
    keyboard_ctrl_press(CtrlKeys.PASTE)

