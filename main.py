import time
import signal
import sys
from core.config.config import Config
from core.broker_adapter import BrokerAdapter
from strategy.trend_strategy import TrendStrategy
from order_management.send_order import place_market_order

def graceful_exit(signal, frame):
    print("\nĐang dừng chương trình một cách an toàn...")
    broker.disconnect()  # Đảm bảo ngắt kết nối với broker khi dừng
    sys.exit(0)  # Thoát chương trình

if __name__ == "__main__":
    config = Config()
    broker = BrokerAdapter(config)
    strategy = TrendStrategy()

    # Đăng ký tín hiệu dừng (Ctrl+C)
    signal.signal(signal.SIGINT, graceful_exit)

    if broker.connect():
        symbols = config.get("symbols")
        
        while True:  # Vòng lặp vô hạn để kiểm tra tín hiệu giao dịch
            for symbol in symbols:
                market_data = broker.get_symbol_data(symbol)
                print(f"Dữ liệu thị trường cho {symbol}: {market_data}")

                signal = strategy.generate_signal(symbol, market_data)
                if signal:
                    print(f"Tín hiệu giao dịch cho {symbol}: {signal}")
                    place_market_order(
                        symbol=symbol,
                        order_type=signal,
                        volume=0.1,
                        sl=0.0,
                        tp=0.0,
                        magic=config.get("magic_number"),
                        comment="Test Order"
                    )
                else:
                    print(f"Không có tín hiệu giao dịch cho {symbol}")
            
            # Chờ 60 giây trước khi tiếp tục vòng lặp
            print("Chờ 60 giây trước khi kiểm tra lại...")
            time.sleep(60)  # Trì hoãn 60 giây
        broker.disconnect()
