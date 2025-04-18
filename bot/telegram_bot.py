from telegram import Bot, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import TelegramError
import logging

logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self, token, chat_id):
        self.bot = Bot(token)
        self.chat_id = chat_id
        
    def send_message(self, text, parse_mode=ParseMode.MARKDOWN, image_url=None, product_url=None):
        try:
            # Se viene fornita un'immagine, invia l'immagine prima del messaggio
            if image_url:
                self.bot.send_photo(chat_id=self.chat_id, photo=image_url)
            
            # Creazione del pulsante "Acquista" con il link al prodotto
            keyboard = []
            if product_url:
                keyboard = [[InlineKeyboardButton("Go to Product", url=product_url)]]
            
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            # Invia il messaggio con il pulsante "Acquista"
            self.bot.send_message(
                chat_id=self.chat_id,
                text=text,
                parse_mode=parse_mode,
                reply_markup=reply_markup
            )
        except TelegramError as e:
            logger.error(f"Failed to send message to Telegram: {str(e)}")
