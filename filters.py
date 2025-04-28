import datetime
from config import MIN_MARKET_CAP, MIN_VOLUME_24H, MAX_AGE_MINUTES, TARGET_DEX

def filter_tokens(tokens):
    filtered = []
    now = datetime.datetime.utcnow()

    for token in tokens:
        try:
            mc = token.get('market_cap', 0)
            vol = token.get('volume_24h', 0)
            launch_time_str = token.get('created_at')
            dex_id = token.get('dex_id', '').lower()

            if not launch_time_str or dex_id != TARGET_DEX:
                continue

            launch_time = datetime.datetime.strptime(launch_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            minutes_since_launch = (now - launch_time).total_seconds() / 60

            if mc >= MIN_MARKET_CAP and vol >= MIN_VOLUME_24H and minutes_since_launch <= MAX_AGE_MINUTES:
                filtered.append(token)
        except Exception as e:
            print(f"Error filtering token: {e}")

    return filtered