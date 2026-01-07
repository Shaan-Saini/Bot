from fetch_data import get_option_chain
from process_data import calculate_pcr
from strategy import trade_signal
from logger import log_signal

def run_bot(use_sample=False):
    source = "SAMPLE" if use_sample else "LIVE"

    if use_sample:
        from sample_data import get_sample_data
        data = get_sample_data()
    else:
        data = get_option_chain("NIFTY")

    if "records" not in data:
        print("❌ DATA NOT AVAILABLE")
        return

    spot = data["records"]["underlyingValue"]
    pcr = calculate_pcr(data)
    signal = trade_signal(pcr)

    print("\n===== OPTION CHAIN BOT =====")
    print("SOURCE     :", source)
    print("SPOT PRICE :", spot)
    print("PCR        :", pcr)
    print("SIGNAL     :", signal)
    print("===========================\n")

    log_signal(spot, pcr, signal, source)

if __name__ == "__main__":
    run_bot(use_sample=True)   # <-- SAMPLE MODE DEFAULT
