# 

# brokers/mt5_api.py

import MetaTrader5 as mt5

class MT5Api:
    def __init__(self, config):
        self.login = config.login
        self.password = config.password
        self.server = config.server

    def connect(self):
        if not mt5.initialize():
            print("Initialize MT5 thất bại.")
            return False
        authorized = mt5.login(self.login, password=self.password, server=self.server)
        if authorized:
            print(f"Đăng nhập vào MT5 thành công với tài khoản {self.login} trên server {self.server}")
            return True
        else:
            print(f"Đăng nhập thất bại, lỗi: {mt5.last_error()}")
            return False

    def disconnect(self):
        mt5.shutdown()

    def get_symbol_data(self):
        symbols = ["EURUSDm", "GBPUSDm", "USDJPYm"]
        market_data = {}
        for symbol in symbols:
            tick = mt5.symbol_info_tick(symbol)
            if tick:
                market_data[symbol] = {
                    "bid": tick.bid,
                    "ask": tick.ask,
                    "last": tick.last,
                    "time": tick.time
                }
            else:
                print(f"Không lấy được dữ liệu cho {symbol}.")
        return market_data
