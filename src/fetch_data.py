import requests
import time
import random

def get_option_chain(symbol="NIFTY", retries=3, base_delay=2):
    """
    Fetch option chain data from NSE with retry + delay.
    Returns dict if successful, else empty dict.
    """

    url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/option-chain",
        "Connection": "keep-alive"
    }

    session = requests.Session()

    # Initial homepage hit (important for cookies)
    try:
        session.get("https://www.nseindia.com", headers=headers, timeout=5)
    except Exception:
        pass

    for attempt in range(1, retries + 1):
        try:
            response = session.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                data = response.json()

                # Valid NSE response check
                if isinstance(data, dict) and "records" in data:
                    return data

        except Exception:
            pass

        # Retry delay (human-like)
        sleep_time = base_delay + random.uniform(0.5, 2.0)
        time.sleep(sleep_time)

    # All retries failed
    return {}
