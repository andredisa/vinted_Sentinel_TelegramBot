# Vinted Sentinel 🚀📦

**Your personal shopping assistant for Vinted!** This powerful bot monitors Vinted products in real-time and sends instant notifications directly to your Telegram. It's not just a bot—it's your **ultimate shopping tool**, designed to save you time and bring you the best Vinted deals as they drop! 🎉💥

🛍️ **Instant Alerts** | 📲 **Real-Time Notifications** | 🎯 **Tailored to Your Needs**

---

### 📣 **Real-time Vinted Monitoring!**

Your **ultimate personal shopping assistant** for tracking new listings on **Vinted**! Whether you're on the lookout for the latest **fashion trends**, rare **collectibles**, or just hunting for a great bargain, the **Vinted Monitor** bot has got you covered! 🌟

> **With this bot, you can:**
- 🔎 **Track products** based on your custom search criteria (e.g., **brands**, **sizes**, **prices**, or **item conditions**).
- ⚡ **Receive instant updates** on new listings with **real-time notifications** sent directly to your **Telegram channel**. 📲
- 🌍 **Monitor listings across multiple countries**, expanding your shopping horizon to regions like **Germany** 🇩🇪, **Italy** 🇮🇹, **France** 🇫🇷, and more!
- 🔄 **Filter results** by **keywords**, **size**, **price**, or **condition**. Let the bot do the work and bring you the best results! 🎯

---

### ✨ **How does it work?**

The **Vinted Monitor** bot connects directly to **Vinted’s API**, performs advanced searches based on your preferences, and continuously monitors for new listings. When a matching product is posted, the bot will instantly notify you via **Telegram**! 📬

---

### 🛠️ **Key Features:**
- **🔍 Customizable Search**: Set your own search terms (e.g., brand names, item types, sizes) and let the bot monitor the listings.
- **🌎 Multi-Country Support**: Track products from multiple regions, like **Germany** 🇩🇪, **France** 🇫🇷, **Italy** 🇮🇹, and more, just by adding them to the configuration file.
- **📲 Telegram Notifications**: Receive detailed notifications in your Telegram channel, complete with **product images**, **descriptions**, **prices**, and direct **purchase links**!
- **⏳ Frequent Updates**: Customize how often the bot checks for new listings (e.g., every **3 minutes**, **10 minutes**, etc.).
- **📊 Duplicate Prevention**: The bot ensures you won’t receive duplicate notifications by tracking already seen products.
- **🛠️ Easy Configuration**: Configure everything in a **JSON file**, including search terms, preferred Telegram channel, and countries.
- **🖼️ Product Details**: Notifications contain the product's title, description, price, images, and a direct link to the product page on Vinted.

---

### 🔥 **Perfect for:**

- **Shoppers** looking for the best deals and new listings that match their interests. 🛍️
- **Vinted enthusiasts** searching for specific items like **designer brands**, **vintage clothes**, or rare **accessories**. 👗
- **Resellers** who need to track valuable or profitable products in real-time. 💼
- **Fashion lovers** eager to know when exciting new items are listed. 💅

---

### 🎯 **What sets Vinted Monitor apart?**
- **🧩 Customizable & User-Friendly**: Easily set up your search terms, monitor multiple countries, and get alerts tailored to your exact needs. 🎯
- **🌍 Multi-Country Support**: Track listings across **Vinted.de**, **Vinted.it**, **Vinted.fr**, and more. No need to visit different marketplaces manually—let the bot do the heavy lifting! 🌏
- **⚡ Instant Telegram Alerts**: Get fast, reliable notifications directly to **Telegram**, complete with product details, images, and purchase links.
- **⏳ 24/7 Monitoring**: The bot runs continuously, checking for updates at intervals you set. Never miss a deal again! 🔄

---

## 🚀 **Installation Guide**

### 1️⃣ **Clone the repository**  
```bash
git clone https://github.com/your-username/vinted_Sentinel_TelegramBot.git
cd vinted-monitor

```
### 2️⃣ Install Dependencies
> Make sure you have Python properly configured, then install the necessary libraries:
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure the bot
> Create the configuration file `config/config.json` with the following parameters:
```json
{
  "token": "your_telegram_bot_token",
  "channel_id": "your_telegram_channel_id",
  "search_terms": ["ralph lauren", "nike", "adidas"],
  "refresh_delay": 3,
  "max_images_per_post": 4,
  "countries": [".de", ".it", ".fr"]
}
```

- `token:` Your Telegram bot token.

- `channel_id:` The ID of the Telegram channel where you want to receive notifications.

- `search_terms:` List of keywords to monitor (e.g., brands, categories).

- `countries:` Countries to monitor (e.g., .de for Germany, .it for Italy).

### 4️⃣ Start the bot
Once configured, run the bot with the following command:

```bash
python main.py
```
> The bot will start monitoring products on Vinted and send notifications to your Telegram channel when new items are found!

---

## ⚙️ Main Features
- 📍 **Multi-Country Monitoring:** Choose from multiple countries to monitor Vinted, such as Germany, Italy, France, and many more. 🇩🇪🇮🇹🇫🇷

- 📸 **Images and Details:** Each notification includes the main image of the product, price, name, description, and a direct link to the product on Vinted.

- 🔁 **Duplicate Prevention:** The bot monitors a product database to avoid duplicate notifications.

- ⏳ **Frequent Updates:** You can adjust how often the bot updates its search in the config file (`refresh_delay`).

---

## 🗂️ Project Structure

```bash
vinted-monitor/
├── config/
│   └── config.json         # Bot configuration file
├── bot/
│   ├── telegram_bot.py     # Sends notifications via Telegram
│   └── vinted_monitor.py   # Logic for monitoring Vinted products
├── db/
│   └── product_database.py # Manages the product database
├── api/
│   └── vinted_api.py      # Interaction with Vinted API
├── main.py                 # Entry point for the bot
└── requirements.txt        # Dependencies
```

---

## 🧩 File Details
- `main.py:` Initializes and starts the bot.

- `config/config.json:` Bot configuration (token, channel, keywords).

- `bot/telegram_bot.py:` Sends notifications on Telegram.

- `api/vinted_api.py:` Manages interaction with Vinted API, supporting multiple countries.

- `db/product_database.py:` Manages the product database to prevent duplicates.

---

## 📦 Requirements
> Install the required dependencies via `requirements.txt`:

- requests: For making HTTP requests to the Vinted API.

- python-telegram-bot: To handle Telegram notifications.

You can install all dependencies by running:

```bash
pip install -r requirements.txt
```

---

## 🔄 Contribute
>If you would like to improve this project, feel free to fork the repository and submit a pull request.

**What you can improve:**
- Add more countries for monitoring.

- Optimize the database handling.

- Improve product search logic for specific categories.

---

## 📝 License
>This project is licensed under the MIT License. You are free to use, modify, and distribute it as you like.

---

> 💬 Feel free to reach out on [GitHub](https://github.com/andredisa) or by [email](mailto:andreadisanti22@gmail.com)!

### 🎉 Enjoy using the Vinted Sentinel! 🎉
