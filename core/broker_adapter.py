# # core/broker_adapter.py

# class BrokerAdapter:
#     def __init__(self, config):
#         self.config = config
#         self.broker_connection = None
    
#     def connect(self):
#         """Kết nối tới broker."""
#         print(f"Đang kết nối với broker {self.config['server']}...")
#         self.broker_connection = True  # Giả sử kết nối thành công
#         return True
    
#     def get_symbol_data(self):
#         """Lấy dữ liệu thị trường của symbol."""
#         if not self.broker_connection:
#             print("Chưa kết nối với broker!")
#             return None
#         return {
#             "EURUSDm": {"bid": 1.14349, "ask": 1.14358, "last": 0.0, "time": 1745346789},
#             "GBPUSDm": {"bid": 1.33417, "ask": 1.33428, "last": 0.0, "time": 1745346790},
#             "USDJPYm": {"bid": 141.299, "ask": 141.309, "last": 0.0, "time": 1745346790}
#         }
    
#     def disconnect(self):
#         """Ngắt kết nối với broker."""
#         self.broker_connection = None
#         print("Đã ngắt kết nối với broker.")


# core/broker_adapter.py

from brokers.mt5_api import MT5Api

class BrokerAdapter:
    def __init__(self, config):
        self.api = MT5Api(config)

    def connect(self):
        return self.api.connect()

    def disconnect(self):
        return self.api.disconnect()

    def get_symbol_data(self):
        return self.api.get_symbol_data()
