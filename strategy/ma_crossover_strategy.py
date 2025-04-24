# strategy/ma_crossover_strategy.py

class MACrossoverStrategy:
    def __init__(self, fast_period=5, slow_period=20):
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.price_history = {}  # Lưu trữ lịch sử giá

    def calculate_ma(self, prices, period):
        return sum(prices[-period:]) / period if len(prices) >= period else None

    def generate_signal(self, symbol, market_data):
        if symbol not in self.price_history:
            self.price_history[symbol] = []

        # Tính giá đóng cửa trung bình
        close_price = (market_data[symbol]['bid'] + market_data[symbol]['ask']) / 2
        self.price_history[symbol].append(close_price)

        # Chưa đủ dữ liệu
        if len(self.price_history[symbol]) < self.slow_period:
            return None

        fast_ma = self.calculate_ma(self.price_history[symbol], self.fast_period)
        slow_ma = self.calculate_ma(self.price_history[symbol], self.slow_period)

        # Nếu không tính được MA
        if fast_ma is None or slow_ma is None:
            return None

        # Lấy giá trị MA trước đó để xác định giao cắt
        prev_fast = self.calculate_ma(self.price_history[symbol][:-1], self.fast_period)
        prev_slow = self.calculate_ma(self.price_history[symbol][:-1], self.slow_period)

        # Giao cắt lên
        if prev_fast < prev_slow and fast_ma > slow_ma:
            return "buy"

        # Giao cắt xuống
        if prev_fast > prev_slow and fast_ma < slow_ma:
            return "sell"

        return None
