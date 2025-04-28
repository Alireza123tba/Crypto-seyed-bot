import time
import threading
from fetcher import fetch_data_mevx, fetch_data_dexscreener
from filters import filter_tokens
from telegram_bot import send_to_telegram
from database import init_db, token_exists, add_token
from server import run_server
from config import DATABASE_FILE, CHECK_INTERVAL

def main_loop():
    init_db(DATABASE_FILE)

    while True:
        tokens_mevx = fetch_data_mevx()
        tokens_dexscreener = fetch_data_dexscreener()
        all_tokens = tokens_mevx + tokens_dexscreener
        good_tokens = filter_tokens(all_tokens)

        for token in good_tokens:
            pair_address = token.get('pair_address')
            if pair_address and not token_exists(DATABASE_FILE, pair_address):
                send_to_telegram(token)
                add_token(DATABASE_FILE, pair_address)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    threading.Thread(target=run_server).start()
    main_loop()