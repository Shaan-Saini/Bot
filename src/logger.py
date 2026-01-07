from datetime import datetime

LOG_FILE = "../logs/signals.log"

def log_signal(spot, pcr, signal, source):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_line = (
        f"{timestamp} | SOURCE={source} | "
        f"SPOT={spot} | PCR={pcr} | SIGNAL={signal}\n"
    )

    with open(LOG_FILE, "a") as f:
        f.write(log_line)
