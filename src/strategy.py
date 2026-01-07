def trade_signal(pcr):
    if pcr is None:
        return "DATA ERROR"

    if pcr > 1.2:
        return "BULLISH → BUY CALL"
    elif pcr < 0.8:
        return "BEARISH → BUY PUT"
    else:
        return "SIDEWAYS → NO TRADE"
