class TrendStrategy:
    def generate_signal(self, symbol, market_data):
        bid = market_data.get("bid")
        ask = market_data.get("ask")

        if bid is None or ask is None:
            return None

        # Tính chênh lệch giá bid và ask
        price_diff = ask - bid
        if price_diff > 0.0001:  # Nếu sự chênh lệch lớn hơn 0.0001
            return "buy"
        elif price_diff < -0.0001:  # Nếu sự chênh lệch nhỏ hơn -0.0001
            return "sell"
        else:
            return None
