import json
import time
from asyncio import run

import ccxt.pro as ccxtpro
import pandas as pd
from notecoin.base.tables.strategy import StrategyTable
from notecoin.task import AccountTask, BaseTask
from notecoin.utils import logger
from notesecret import read_secret


class Strategy2Task(BaseTask):

    def __init__(self, *args, **kwargs):
        super(Strategy2Task, self).__init__(*args, **kwargs)
        self.table = StrategyTable(db_suffix=self.exchange.name)
        self.table.create()

        self.residue = 0
        self.strategy_df = None
        self.update_account()

    def update_account(self):
        AccountTask().refresh()
        account = pd.read_sql(sql=f"select * from {AccountTask.table_name}", con=self.engine.connect())
        for symbol in json.loads(account.to_json(orient='records')):
            if symbol['symbol'] == 'BUSD':
                self.residue = symbol['free']
                break

        self.strategy_df = pd.read_sql(f"select * from {self.table.table_name} where status>2",
                                       con=self.engine.connect())

    def buy_auto(self, price_map):
        if self.residue < 12:
            return
        try:
            self.buy_market("BTC/BUSD", 12)
            logger.info("buy BTC/BUSD success")
        except Exception as e:
            return

    def sell_auto(self, price_map):
        print(price_map)
        for row in json.loads(self.strategy_df.to_json(orient='records')):
            try:
                symbol = row['symbol']
                if symbol not in price_map.keys():
                    continue
                price = price_map[symbol]

                buy_info = json.loads(row['buy_json'])
                buy_price = buy_info['price']
                amount = buy_info['amount']
                timestamp = buy_info['timestamp']
                if time.time() * 1000 - timestamp > 10 * 60 * 1000 and abs((buy_price - price) / price) > 0:
                    logger.info(f"out of time,sell {buy_price} vs {price}")
                    self.sell_market(row['id'], symbol, amount)
                elif abs((buy_price - price) / price) > 0.0005:
                    logger.info(f"buy price {buy_price} vs {price}")
                    self.sell_market(row['id'], symbol, amount)
            except Exception as e:
                logger.info(f"sell error {e}")

    def buy_market(self, symbol, dollar):
        price = self.current_price(symbol)
        if price == 0:
            return
        amount = dollar / price
        buy_json = self.exchange.create_order(symbol, 'market', 'buy', amount)
        value = {
            "status": 2,
            "ext_json": {},
            "symbol": symbol,
            "amount": amount,
            "buy_json": buy_json,
        }
        self.table.upsert(value=value)
        self.update_account()

    def sell_market(self, id, symbol, amount):
        logger.info(f"sell {symbol}")

        sell_json = self.exchange.create_order(symbol, 'market', 'sell', amount)
        value = {
            "id": id,
            "status": 3,
            "sell_json": sell_json,
        }
        self.table.upsert(value=value)
        self.update_account()

    async def watch_symbol(self, symbol='BTC/BUSD', amount=0.0015):
        d = {
            'newUpdates': False,
            'apiKey': read_secret('coin', 'binance', 'api_key'),
            'secretKey': read_secret('coin', 'binance', 'secret_key')
        }
        exchange = ccxtpro.binance(d)
        await exchange.watch_trades(symbol)
        # await exchange.watch_trades('ETC/USDT')

        while True:
            try:
                trades = exchange.trades
                price_map = {}
                for sym in trades.keys():
                    price_map[sym] = float(trades[sym][-1]['info']['p'])
                self.buy_auto(price_map)
                self.sell_auto(price_map)
                await exchange.sleep(10000)
            except Exception as e:
                print(e)

    def run_job(self):
        run(self.watch_symbol())
