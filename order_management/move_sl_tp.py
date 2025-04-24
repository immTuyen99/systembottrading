# order_management/move_sl_tp.py

def move_stop_loss(symbol, new_sl, order_id, broker):
    """
    Dời Stop Loss của lệnh đang mở.
    
    :param symbol: Tên symbol (ví dụ 'EURUSD')
    :param new_sl: Mức giá mới cho Stop Loss
    :param order_id: ID của lệnh đang mở
    :param broker: Đối tượng broker kết nối
    """
    # Lấy thông tin lệnh hiện tại
    order = broker.get_order(order_id)
    
    if order:
        broker.modify_order(
            order_id=order_id,
            sl=new_sl  # Chỉ thay đổi SL, TP không thay đổi
        )
        print(f"Đã dời SL của lệnh {order_id} với {symbol} tới {new_sl}")
    else:
        print(f"Không tìm thấy lệnh với ID {order_id}")

def move_take_profit(symbol, new_tp, order_id, broker):
    """
    Dời Take Profit của lệnh đang mở.
    
    :param symbol: Tên symbol (ví dụ 'EURUSD')
    :param new_tp: Mức giá mới cho Take Profit
    :param order_id: ID của lệnh đang mở
    :param broker: Đối tượng broker kết nối
    """
    # Lấy thông tin lệnh hiện tại
    order = broker.get_order(order_id)
    
    if order:
        broker.modify_order(
            order_id=order_id,
            tp=new_tp  # Chỉ thay đổi TP, SL không thay đổi
        )
        print(f"Đã dời TP của lệnh {order_id} với {symbol} tới {new_tp}")
    else:
        print(f"Không tìm thấy lệnh với ID {order_id}")
