import requests
import time
import json

# 🔄 Replace with your Power BI Push URL
powerbi_url = "https://api.powerbi.com/beta/a64aeab6-f01b-462b-aa9c-44546386ff31/datasets/907c2814-76b4-4ff4-ab83-c1e705a483b7/rows?experience=power-bi&clientSideAuth=0&key=uGCcCkt6oGfCiI69IpALF9zvPE0oyuIaDQjlhFxhW8RhA2fR0%2FuO6pX6qKDahkF1UGnQkBKewq%2FeuHycv3xZJQ%3D%3D"

# 🎯 Crypto symbol
symbol = "BTCUSDT"

def get_price():
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url, timeout=5)

    # If Binance returns empty or blocked
    if response.status_code != 200:
        return None

    data = response.json()
    return float(data["price"])

while True:
    price = get_price()

    if price is None:
        print("⚠️ No data returned. Retrying...")
        time.sleep(3)
        continue

    payload = [{
        "crypto": "BITCOIN",
        "price": price,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }]

    try:
        requests.post(powerbi_url, json=payload)
        print(f"✅ Sent: {payload}")
    except Exception as e:
        print("❌ Error sending to Power BI:", e)

    time.sleep(2)
