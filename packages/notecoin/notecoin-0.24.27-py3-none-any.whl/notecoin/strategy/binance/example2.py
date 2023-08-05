# Python
import time
from asyncio import run

import ccxt.pro as ccxtpro
from notesecret import read_secret


async def main():
    d = {
        'newUpdates': False,
        'apiKey': read_secret('coin', 'binance', 'api_key'),
        'secretKey': read_secret('coin', 'binance', 'secret_key')
    }
    exchange = ccxtpro.binance(d)
    await exchange.watch_trades('BTC/USDT')
    await exchange.watch_trades('ETC/USDT')
    while True:
        try:
            trades = exchange.trades
            # trades = await exchange.watch_trades('BTC/USDT')
            print((1, len(trades['BTC/USDT']), len(trades['ETC/USDT'])))

            # orderbook = await exchange.watch_ohlcv('BTC/USD')
            # orderbook = await exchange.watch_orders()

            # orderbook = await exchange.watch_order_book('BTC/USD')
            # print(orderbook['asks'][0], orderbook['bids'][0])
            # print(await exchange.watch_trades('BTC/USDT'))
            # await exchange.sleep(5)
            time.sleep(1)
            await exchange.sleep(100)
        except Exception as e:
            print(e)


run(main())
print('3232')
