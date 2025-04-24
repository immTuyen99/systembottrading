# strategy/trend_strategy.py

class TrendStrategy:
    def generate_signal(self, symbol, market_data):
        # Ví dụ đơn giản: nếu bid > ask thì bán, ngược lại mua
        bid = market_data.get("bid")
        ask = market_data.get("ask")

        if bid and ask:
            if bid > ask:
                return "sell"
            elif ask > bid:
                return "buy"
        return None
