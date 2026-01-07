def calculate_pcr(data):
    ce_oi = 0
    pe_oi = 0

    for item in data["records"]["data"]:
        if "CE" in item:
            ce_oi += item["CE"]["openInterest"]
        if "PE" in item:
            pe_oi += item["PE"]["openInterest"]

    if ce_oi == 0:
        return None

    return round(pe_oi / ce_oi, 2)
