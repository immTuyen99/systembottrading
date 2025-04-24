# order_management/send_order.py

import MetaTrader5 as mt5

def place_market_order(symbol, order_type, volume, sl=0.0, tp=0.0, magic=123456, comment="Test Order"):
    order_type_mt5 = mt5.ORDER_TYPE_BUY if order_type.lower() == "buy" else mt5.ORDER_TYPE_SELL

    tick = mt5.symbol_info_tick(symbol)
    if not tick:
        print(f"Lỗi: Không lấy được giá cho {symbol}")
        return False

    print(f"Gửi lệnh {order_type} cho {symbol} với khối lượng {volume}")

    price = tick.ask if order_type_mt5 == mt5.ORDER_TYPE_BUY else tick.bid

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type_mt5,
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
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Lỗi gửi lệnh: {result.retcode}, {result.comment}")
        return False
    else:
        print(f"Lệnh {order_type.upper()} được gửi thành công: {result.order}")
        return True
