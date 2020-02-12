import json
import requests

ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array'

limit = 100
start = 1
sort = 'id'
convert = 'USD'

choice = input('Do you want to enter any custom parameters? (y/n): ')

if choice == 'y':
    limit   = input(f'New value for limit ({limit})           : ') and limit
    start   = input(f'New value for start from ({start})      : ') and start
    sort    = input(f'New value for sort by ({sort})          : ') and sort
    convert = input(f'New value for local currency ({convert}): ') and convert

ticker_url += f'&limit={limit}&start={start}&sort={sort}&convert={convert}'

request = requests.get(ticker_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']
print()

for currency in data:
    rank = currency['rank']
    name = currency['name']
    symbol = currency['symbol']

    circulating_supply = int(currency['circulating_supply'])
    total_supply = int(currency['total_supply'])

    quotes = currency['quotes'][convert]

    market_cap = quotes['market_cap']
    hour_change = quotes['percent_change_1h']
    day_change = quotes['percent_change_24h']
    week_change = quotes['percent_change_7d']
    price = quotes['price']
    volume = quotes['volume_24h']

    print(f'{rank:>5} {name} ({symbol})')
    print(f'Market Cap: {convert} {market_cap:,}')
    print(f'Price: {convert} {price}')
    print(f'Volume: {volume}')
    print(f'Hour change: {hour_change}%')
    print(f'Day change: {day_change}%')
    print(f'Week change: {week_change}%')

    print(f'Total supply: {total_supply}')
    print(f'Circulating supply: {circulating_supply}')

    print(f'Percentage of coins in circulation: {circulating_supply/total_supply*100: .2}%')
