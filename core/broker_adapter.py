from brokers.mt5_api import MT5Api

class BrokerAdapter:
    def __init__(self, config):
        self.api = MT5Api(config)

    def connect(self):
        return self.api.connect()

    def disconnect(self):
        return self.api.disconnect()

    def get_symbol_data(self, symbol):
        return self.api.get_symbol_data(symbol)
