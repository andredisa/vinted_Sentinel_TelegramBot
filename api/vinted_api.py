import requests
import logging

logger = logging.getLogger(__name__)

class VintedAPI:
    def __init__(self, country_code=".de"):
        self.session = requests.Session()
        self.token: Optional[str] = None
        self.base_url = f"https://www.vinted{country_code}"  # URL dinamico in base al paese
    
    def _get_headers(self, with_auth: bool = False) -> Dict:
        headers = {
            'Host': f'www.vinted{self.country_code}',
            'x-app-version': '24.43.1',
            'accept': 'application/json',
            'accept-language': 'de-fr',
            'user-agent': 'vinted-ios Vinted/24.43.1 (lt.manodrabuziai.de; build:30115; iOS 18.2.0) iPad13,6',
            'x-device-model': 'iPad13,6'
        }
        
        if with_auth and self.token:
            headers['authorization'] = f'Bearer {self.token}'
            
        return headers
    
async def search_products(self, search_text: str) -> List[Dict]:
    try:
        params = {
            'page': '1',
            'per_page': '10',
            'search_text': search_text,
            'order': 'newest_first',
        }
        
        response = self.session.get(
            f'{self.base_url}/api/v2/catalog/items',
            params=params,
            headers=self._get_headers(with_auth=True)
        )
        response.raise_for_status()
        data = response.json()
        
        # Estrazione dell'URL dell'immagine, se disponibile
        items = []
        for item in data.get('items', []):
            image_url = item.get('photos', [{}])[0].get('url', None)
            item['image_url'] = image_url  # Aggiungi l'URL dell'immagine all'item
            items.append(item)
        
        return items
    except Exception as e:
        logger.error(f"Failed to search products: {str(e)}")
        return []
