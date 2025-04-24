from collections import deque

class TrendStrategy:
    def __init__(self):
        self.price_history = {}  # Lưu lịch sử giá cho mỗi symbol
        self.window_size = 5     # Số lượng nến để tính MA

    def generate_signal(self, symbol, data):
        bid = data.get('bid')
        if bid is None:
            return None

        # Khởi tạo deque nếu chưa có
        if symbol not in self.price_history:
            self.price_history[symbol] = deque(maxlen=self.window_size)
        
        # Cập nhật giá mới
        self.price_history[symbol].append(bid)

        # Chờ đủ dữ liệu MA
        if len(self.price_history[symbol]) < self.window_size:
            return None

        # Tính trung bình MA
        sma = sum(self.price_history[symbol]) / self.window_size

        # Tín hiệu đơn giản: bid vượt lên hoặc cắt xuống MA
        if bid > sma:
            return "buy"
        elif bid < sma:
            return "sell"
        else:
            return None
