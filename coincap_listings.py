import json
import requests

# from datetime import datetime

listings_url = 'https://api.coinmarketcap.com/v2/listings/'

request = requests.get(listings_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']

for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    slug = currency['website_slug']

    print(f'{rank:5} : {name} ({symbol})')
