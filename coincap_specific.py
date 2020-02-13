import requests
import json

convert = 'USD'
listings_url = 'https://api.coinmarketcap.com/v2/listings/'

request = requests.get(listings_url)
results = request.json()

data = results['data']
ticket_url_pairs = { currency['symbol']:currency['id'] for currency in data }

print(ticket_url_pairs)

# while True:

print()
choice = input("Enter the ticker symbol of cryptocurrency: ").upper()

ticket_url = f'https://api.coinmarketcap.com/v2/ticker/{ticket_url_pairs[choice]}/?strucure=array&convert={convert}'
request = requests.get(ticket_url)
results = request.json()


data = results['data']
print(json.dumps(data, sort_keys=True, indent=4))




# print(f'{rank:>5}           {name} ({symbol})')
# print(f'Market Cap:         {convert} {market_cap:,}')
# print(f'Price:              {convert} {price}')
# print(f'Volume:             {volume}')
# print(f'Hour change:        {hour_change}%')
# print(f'Day change:         {day_change}%')
# print(f'Week change:        {week_change}%')

# print(f'Total supply:       {total_supply}')
# print(f'Circulating supply: {circulating_supply}')

# print(f'Percentage of coins in circulation: {circulating_supply/total_supply*100:3.2f}%')
# print('-'*30)
# print()

