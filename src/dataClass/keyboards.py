from dataclasses import dataclass
from typing import List

from telebot import types

from src.dataClass import keys

keys = keys.Keys()

@dataclass
class Keyboards:
    main:List = create_keyboard(keys.random_connect, keys.setting)
    
def create_keyboard(*keys, row_width=2, resize_keyboard=True):
    markup =  types.ReplyKeyboardMarkup(
        row_width=row_width,
        resize_keyboard=resize_keyboard
    )
    
    buttons = map(types.KeyboardButton, keys)
    markup.add(*buttons)
    
    return markup