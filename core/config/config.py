# core/config/config.py

class Config:
    def __init__(self):
        self.login = 244575425
        self.password = "dmT290699@"
        self.server = "Exness-MT5Trial14"
        self.symbols = ["EURUSDm", "GBPUSDm", "USDJPYm"]
        self.risk_percent = 2.0
        self.magic_number = 123456

    def get(self, key, default=None):
        return getattr(self, key, default)
