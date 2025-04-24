# # main.py

# from core.config.config import Config
# from core.broker_adapter import BrokerAdapter

# if __name__ == "__main__":
#     config = Config()
#     broker = BrokerAdapter(config)

#     if broker.connect():
#         market_data = broker.get_symbol_data()
#         print(f"Dữ liệu thị trường: {market_data}")
#         broker.disconnect()


from core.config.config import Config
from core.broker_adapter import BrokerAdapter
from strategy.trend_strategy import TrendStrategy
from order_management.send_order import place_market_order
import time

if __name__ == "__main__":
    # Load cấu hình và kết nối broker
    config = Config()
    broker = BrokerAdapter(config)

    if broker.connect():
        print("Kết nối với broker thành công!")

        # Khởi tạo chiến lược giao dịch
        strategy = TrendStrategy()

        # Vòng lặp chính
        while True:
            try:
                # Lấy dữ liệu thị trường
                market_data = broker.get_symbol_data()
                print(f"Dữ liệu thị trường: {market_data}")

                # Phân tích tín hiệu và gửi lệnh nếu có tín hiệu
                for symbol, data in market_data.items():
                    signal = strategy.generate_signal(symbol, data)

                    # Nếu có tín hiệu mua hoặc bán, gửi lệnh
                    if signal == "buy":
                        print(f"[{symbol}] Có tín hiệu MUA → Gửi lệnh")
                        place_market_order(symbol, 0.01, order_type=0)  # 0 = Mua
                    elif signal == "sell":
                        print(f"[{symbol}] Có tín hiệu BÁN → Gửi lệnh")
                        place_market_order(symbol, 0.01, order_type=1)  # 1 = Bán
                    else:
                        print(f"[{symbol}] Không có tín hiệu.")

                # Delay giữa các lần quét
                time.sleep(10)

            except Exception as e:
                print("Lỗi trong vòng lặp:", str(e))
                break

        # Ngắt kết nối khi kết thúc
        broker.disconnect()
    else:
        print("Không thể kết nối với broker!")
