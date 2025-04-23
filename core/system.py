# # core/system.py

# from core.broker_adapter import BrokerAdapter
# from core.config.config import CONFIG

# class TradingSystem:
#     def __init__(self):
#         self.broker_adapter = BrokerAdapter(CONFIG["broker"])
#         self.market_data = {}

#     def connect(self):
#         """Kết nối với broker."""
#         if self.broker_adapter.connect():
#             print("Kết nối với broker thành công!")
#         else:
#             print("Kết nối thất bại!")

#     def get_market_data(self):
#         """Lấy dữ liệu thị trường từ broker."""
#         self.market_data = self.broker_adapter.get_market_data()
#         print("Dữ liệu thị trường:", self.market_data)

#     def close(self):
#         """Đóng kết nối với broker."""
#         self.broker_adapter.close()

# core/system.py

from core.broker_adapter import BrokerAdapter

class BrokerManager:
    def __init__(self, config):
        self.config = config
        self.broker_adapter = BrokerAdapter(config)
    
    def connect(self):
        """Kết nối với broker thông qua BrokerAdapter."""
        return self.broker_adapter.connect()
    
    def get_symbol_data(self):
        """Lấy dữ liệu thị trường thông qua BrokerAdapter."""
        return self.broker_adapter.get_symbol_data()
    
    def disconnect(self):
        """Ngắt kết nối với broker."""
        self.broker_adapter.disconnect()
