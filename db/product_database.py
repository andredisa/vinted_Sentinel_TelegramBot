import json
from datetime import datetime
from pathlib import Path
from typing import Dict

class ProductDatabase:
    def __init__(self, file_path: str = "products.json"):
        self.file_path = Path(file_path)
        self.seen_products: Dict[str, Dict] = self._load_database()

    def _load_database(self) -> Dict[str, Dict]:
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_database(self):
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.seen_products, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving database: {str(e)}")

    def is_product_seen(self, product_id: str) -> bool:
        return product_id in self.seen_products

    def add_product(self, product):
        try:
            self.seen_products[product['id']] = {
                "data": product,
                "timestamp": datetime.now().isoformat()
            }
            self.save_database()
        except Exception as e:
            logger.error(f"Error adding product to database: {str(e)}")
