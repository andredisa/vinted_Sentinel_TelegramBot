import json
import logging
import asyncio
from bot.vinted_monitor import VintedMonitor

logging.basicConfig(level=logging.INFO)

def main():
    try:
        with open('config/config.json') as f:
            config = json.load(f)
        
        monitor = VintedMonitor(config)
        asyncio.run(monitor.start_monitoring())
        
    except Exception as e:
        logging.error(f"Error starting the bot: {str(e)}")

if __name__ == "__main__":
    main()
