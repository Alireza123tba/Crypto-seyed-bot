import requests

def fetch_data_mevx():
    url = 'https://api.mevx.io/v1/pairs'
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error fetching MEVX: {e}")
    return []

def fetch_data_dexscreener():
    url = 'https://api.dexscreener.com/latest/dex/tokens'
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error fetching Dexscreener: {e}")
    return []