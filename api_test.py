import requests

# Base URL of the API
BASE_URL = 'http://127.0.0.1:8000/api/stocks/'

def create_stock(ticker, name, price):
    """Create a new stock."""
    payload = {
        "ticker": ticker,
        "name": name,
        "price": price
    }
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        print(f"Stock created: {response.json()}")
    else:
        print(f"Failed to create stock: {response.status_code}, {response.json()}")
