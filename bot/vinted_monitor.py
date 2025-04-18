import asyncio
from api.vinted_api import VintedAPI
from bot.telegram_bot import TelegramBot
from db.product_database import ProductDatabase
import logging

logger = logging.getLogger(__name__)

class VintedMonitor:
    def __init__(self, config):
        self.config = config
        self.db = ProductDatabase()
        self.bot = TelegramBot(config['token'], config['channel_id'])

    async def start_monitoring(self):
        while True:
            try:
                for country_code in self.config['countries']:
                    # Iniziamo una nuova sessione API per ciascun paese
                    self.api = VintedAPI(country_code)
                    
                    for search_term in self.config['search_terms']:
                        logger.debug(f"Searching for term: {search_term} in {country_code}")
                        items = await self.api.search_products(search_term)
                        
                        for item in items:
                            try:
                                item_id = str(item.get('id'))
                                if not item_id or self.db.is_product_seen(item_id):
                                    continue
                                
                                self.db.add_product(item)
                                
                                message_text = self.create_message(item, country_code)
                                self.bot.send_message(message_text)
                                logger.info(f"New product found and posted: {item.get('title')}")
                            except Exception as e:
                                logger.error(f"Error processing item: {str(e)}")
                                continue

                await asyncio.sleep(self.config['refresh_delay'])
                
            except Exception as e:
                logger.error(f"Error in monitoring loop: {str(e)}")
                await asyncio.sleep(30)
    
    def create_message(self, item, country_code):
        country_name = self.get_country_name_from_code(country_code)
        return f"New Product in {country_name}: {item['title']}\nPrice: {item['price']}€\nCountry: {country_name}\nLink: {item['url']}"

    def get_country_name_from_code(self, country_code):
        country_map = {
            ".de": "Germany",
            ".it": "Italy",
            ".fr": "France",
            ".es": "Spain",
            ".uk": "United Kingdom"
        }
        return country_map.get(country_code, "Unknown Country")
