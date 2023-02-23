import telebot
import os
from loguru import logger

class Bot:
    
    def __init__(self) -> None:
        self.bot = telebot.TeleBot(os.environ['ANONYMOUS_BOT_TOKEN'])
    
    def run(self):
        logger.info('Bot is running...')
        self.bot.infinity_polling()
        

if __name__=='__main__':
	logger.info('Bot Started')
	bot = Bot()
	bot.run()