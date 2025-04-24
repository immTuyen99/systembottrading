# CONFIG = {
#     "broker": "MT5",
#     "login": 244575425,  # Sửa từ "244575425" thành 244575425
#     "password": "dmT290699@",  
#     "server": "Exness-MT5Trial14",  
#     "symbols": ["EURUSDm", "GBPUSDm", "USDJPYm"],  
#     "risk_percent": 2.0,  
#     "magic_number": 123456,  
# }

# # core/config/config.py

# class Config:
#     def __init__(self):
#         self.config = {
#             "login": 244575425,
#             "password": "dmT290699@",
#             "server": "Exness-MT5Trial14",
#             "symbol": "EURUSDm"
#         }

#     def get(self, key, default=None):
#         """Lấy giá trị cấu hình theo key."""
#         return self.config.get(key, default)

# core/config/config.py

# core/config/config.py

class Config:
    def __init__(self):
        self.login = 244575425
        self.password = "dmT290699@"
        self.server = "Exness-MT5Trial14"
        self.symbols = ["EURUSDm", "GBPUSDm", "USDJPYm"]
        self.risk_percent = 2.0
        self.magic_number = 123456
        self.default_volume = 0.1  # bạn có thể thêm cái này nếu cần

    def get(self, key, default=None):
        return getattr(self, key, default)


