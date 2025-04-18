from telegram import Bot, ParseMode
from telegram.error import TelegramError
import logging

logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self, token, chat_id):
        self.bot = Bot(token)
        self.chat_id = chat_id
        
    def send_message(self, text, parse_mode=ParseMode.MARKDOWN):
        try:
            self.bot.send_message(chat_id=self.chat_id, text=text, parse_mode=parse_mode)
        except TelegramError as e:
            logger.error(f"Failed to send message to Telegram: {str(e)}")
