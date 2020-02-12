import json
import requests

from datetime import datetime

currency = 'EUR'
global_url = 'https://api.coinmarketcap.com/v2/global/?convert='+currency

request = requests.get(global_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

active_cryptocurrencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap_usd = int(results['data']['quotes']['USD']['total_market_cap'])
global_cap_cur = int(results['data']['quotes'][currency]['total_market_cap'])
global_volume_usd = int(results['data']['quotes']['USD']['total_volume_24h'])
global_volume_cur = int(results['data']['quotes'][currency]['total_volume_24h'])

last_updated_str = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M:%S %p')

print()
print(f'There are currently {active_cryptocurrencies:,} cryptocurrencies and {active_markets:,} markets')
print(f'The global cap of all cryptos is {global_cap_usd:,} and 24h global volume is {global_volume_usd:,}.')
# print(f'The global cap of all cryptos is {currency} {global_cap_cur:,} and 24h global volume is {currency} {global_volume_cur:,}.')
print(f'Bitcoin\'s total percentage of the global cap is {bitcoin_percentage:,}%.')
print()
print(f'Last updated: {last_updated_str}')


# print(f'Active Cryptocurrencies: {active_cryptocurrencies}')