import MetaTrader5 as mt5  # Thêm import thư viện MetaTrader5

class MT5Api:
    def __init__(self, config):
        self.config = config
        self.connection = None
    
    def connect(self):
        """Kết nối tới MT5."""
        server = self.config.get('server')  # Lấy server từ config bằng phương thức get()
        print(f"Đang kết nối với {server}...")
        if not mt5.initialize():  # Đảm bảo MT5 được khởi tạo
            print("Không thể kết nối với MetaTrader 5")
            return False
        self.connection = True
        return True
    
    def disconnect(self):
        """Ngắt kết nối MT5."""
        if self.connection:
            mt5.shutdown()  # Ngắt kết nối với MT5
            print("Đã ngắt kết nối MT5.")
            self.connection = None
    
    def get_symbol_data(self, symbol):
        if not self.connection:
            print("Chưa kết nối với MT5!")
            return None
        # Lấy dữ liệu thật từ MT5
        symbol_info = mt5.symbol_info_tick(symbol)
        if symbol_info is None:
            print(f"Không thể lấy thông tin cho {symbol}")
            return None
        return {
            symbol: {
                "bid": symbol_info.bid,
                "ask": symbol_info.ask,
                "last": symbol_info.last,
                "time": symbol_info.time
            }
        }
