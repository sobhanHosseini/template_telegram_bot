import os

import telebot
from loguru import logger
from telebot import types

from src.utils.io import write_json

markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard= True)
itembtn1 = types.KeyboardButton('Connect')
itembtn2 = types.KeyboardButton('Settings')
markup.add(itembtn1, itembtn2)

class Bot:
    
    def __init__(self) -> None:
        self.bot = telebot.TeleBot(os.environ['ANONYMOUS_BOT_TOKEN'])
        self.echo_all = self.bot.message_handler(func=lambda message: True)(self.echo_all)
    
    def run(self):
        logger.info('Bot is running...')
        self.bot.infinity_polling()
    
    def echo_all(self, message):
        self.bot.send_message(
            message.chat.id, message.text,
            reply_markup=markup
            )
		
if __name__ == '__main__':
	logger.info('Bot Started')
	bot = Bot()
	bot.run()