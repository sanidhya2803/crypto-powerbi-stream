import requests
import time
from datetime import datetime

power_bi_url = "https://api.powerbi.com/beta/a64aeab6-f01b-462b-aa9c-44546386ff31/datasets/907c2814-76b4-4ff4-ab83-c1e705a483b7/rows?experience=power-bi&key=uGCcCkt6oGfCiI69IpALF9zvPE0oyuIaDQjlhFxhW8RhA2fR0%2FuO6pX6qKDahkF1UGnQkBKewq%2FeuHycv3xZJQ%3D%3D"

def get_price(symbol="BTC-USDT"):
    url = f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={symbol}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    data = r.json()
    return float(data["data"]["price"])

while True:
    try:
        price = get_price("BTC-USDT")
        timestamp = datetime.utcnow().isoformat()

        payload = [{
            "crypto": "BITCOIN",
            "price": price,
            "timestamp": timestamp
        }]

        requests.post(power_bi_url, json=payload)
        print(f"✅ Sent → BITCOIN = {price}")

    except Exception as e:
        print("Error:", e)

    time.sleep(2)   # Update every 2 seconds
