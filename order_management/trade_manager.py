# order_management/trade_manager.py
from order_management.fixed_sl_tp import FixedSLTP
from order_management.close_all_orders import close_all_open_orders
from order_management.send_order import place_market_order
# order_management/trade_manager.py
from order_management.move_sl_tp import move_stop_loss, move_take_profit


class TradeManager:
    def __init__(self, broker, strategy, default_sl=10, default_tp=30):
        self.broker = broker
        self.strategy = strategy
        self.default_sl = default_sl  # SL mặc định
        self.default_tp = default_tp  # TP mặc định

    def execute_trade(self, symbol, signal, volume=0.1, sl=None, tp=None, magic=12345, comment="Test Order"):
        """
        Thực thi giao dịch, bao gồm mở lệnh, dời SL/TP nếu cần.
        """
        if sl is None:
            sl = self.default_sl  # Nếu không có SL riêng, dùng SL mặc định
        if tp is None:
            tp = self.default_tp  # Nếu không có TP riêng, dùng TP mặc định

        order_id = place_market_order(
            symbol=symbol,
            order_type=signal,
            volume=volume,
            sl=sl,
            tp=tp,
            magic=magic,
            comment=comment
        )

        # Dời SL/TP nếu cần
        if signal == 'buy':  # Ví dụ: nếu tín hiệu là 'buy', ta sẽ dời SL/TP
            move_stop_loss(symbol, new_sl=sl + 5, order_id=order_id, broker=self.broker)  # dời SL lên 5 pips
            move_take_profit(symbol, new_tp=tp + 10, order_id=order_id, broker=self.broker)  # dời TP lên 10 pips

    def close_all_trades(self):
        """
        Đóng tất cả các lệnh mở.
        """
        close_all_open_orders(self.broker)
