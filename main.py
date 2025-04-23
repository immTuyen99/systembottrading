# main.py

from core.config.config import Config
from core.broker_adapter import BrokerAdapter

if __name__ == "__main__":
    config = Config()
    broker = BrokerAdapter(config)

    if broker.connect():
        market_data = broker.get_symbol_data()
        print(f"Dữ liệu thị trường: {market_data}")
        broker.disconnect()
