from app.config import *


def keyboard_gen(buttons: list[str]) -> ReplyKeyboardMarkup:
    keyboard_buttons = [KeyboardButton(text=button) for button in buttons]
    return ReplyKeyboardMarkup(keyboard=[keyboard_buttons], resize_keyboard=True)
