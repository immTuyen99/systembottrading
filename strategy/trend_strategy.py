# strategy/trend_strategy.py

class TrendStrategy:
    def generate_signal(self, symbol, market_data):
        bid = market_data.get("bid")
        ask = market_data.get("ask")

        if bid is None or ask is None:
            return None

        if bid > ask:
            return "buy"
        elif ask > bid:
            return "sell"
        else:
            return None
