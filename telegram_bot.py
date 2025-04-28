from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_IDS

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def send_to_telegram(token):
    name = token.get('name', 'Unknown')
    symbol = token.get('symbol', '')
    mc = token.get('market_cap', 0)
    vol = token.get('volume_24h', 0)
    url_link = token.get('url', '')
    image_url = token.get('image_url', '')

    message = (
        f"""🚀 *New GEM Alert!*

"
        f"*Name:* {name}
"
        f"*Symbol:* {symbol}
"
        f"*Market Cap:* ${mc:,.0f}
"
        f"*Volume 24h:* ${vol:,.0f}
"
        f"[View Token]({url_link})"""
    )

    for chat_id in TELEGRAM_CHANNEL_IDS:
        try:
            if image_url:
                bot.send_photo(chat_id=chat_id, photo=image_url, caption=message, parse_mode='Markdown')
            else:
                bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
try:
    # برخی عملیات که ممکن است خطا ایجاد کنند
    some_code()
except Exception as e:
    # در صورت خطا
    print(f"Error: {e}")