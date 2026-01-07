from fetch_data import get_option_chain
from process_data import calculate_pcr
from strategy import trade_signal
from logger import log_signal

def run_bot():
    data = get_option_chain("NIFTY")

    # If live data not available, exit silently
    if not data or "records" not in data:
        print("LIVE DATA NOT AVAILABLE — EXITING")
        return

    spot = data["records"]["underlyingValue"]
    pcr = calculate_pcr(data)
    signal = trade_signal(pcr)

    print("\n===== LIVE OPTION CHAIN BOT =====")
    print("SOURCE     : LIVE NSE")
    print("SPOT PRICE :", spot)
    print("PCR        :", pcr)
    print("SIGNAL     :", signal)
    print("================================\n")

    log_signal(spot, pcr, signal, "LIVE_NSE")

if __name__ == "__main__":
    run_bot()
