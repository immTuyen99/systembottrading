# main.py
import time
from core.config.config import Config
from core.broker_adapter import BrokerAdapter
from strategy.trend_strategy import TrendStrategy
from order_management.send_order import place_market_order
from strategy.ma_crossover_strategy import MACrossoverStrategy  # Thay đổi ở đây
from order_management.trade_manager import TradeManager



if __name__ == "__main__":
    config = Config()  # Tạo đối tượng config
    broker = BrokerAdapter(config)  # Chuyển config vào broker
    strategy = TrendStrategy()
    trade_manager = TradeManager(broker, strategy)  # Khởi tạo TradeManager
    

    try:
        if broker.connect():
            symbols = config.symbols  # Lấy danh sách symbol từ config
            while True:
                for symbol in symbols:
                    market_data = broker.get_symbol_data(symbol)
                    print(f"Dữ liệu thị trường cho {symbol}")  #: {market_data}

                    signal = strategy.generate_signal(symbol, market_data)
                    if signal:
                        print(f"Tín hiệu giao dịch cho {symbol}: {signal}")
                        # Thực thi giao dịch thông qua TradeManager mà không cần thiết lập SL/TP ở đây
                        trade_manager.execute_trade(symbol, signal)
                    else:
                        print(f"Không có tín hiệu giao dịch cho {symbol}")
                
                print("Đang chờ 60 giây để lấy dữ liệu mới...")
                time.sleep(60)
    except KeyboardInterrupt:
        print("Dừng bởi người dùng.")
    finally:
        broker.disconnect()
