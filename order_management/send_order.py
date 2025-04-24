
from order_management.send_order import place_market_order

import MetaTrader5 as mt5

def place_market_order(symbol, order_type, volume):
    # Lệnh mua hoặc bán theo thị trường
    print(f"Gửi lệnh {order_type} cho {symbol} với khối lượng {volume}")    price = mt5.symbol_info_tick(symbol).ask if order_type == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(symbol).bid

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": magic,
        "comment": comment,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    return result
