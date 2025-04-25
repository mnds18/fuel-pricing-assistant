def check_margin_threshold(price, cost, volume, threshold=0.20):
    margin = (price - cost) * volume
    if margin >= threshold * volume:
        return "✅ Meets margin target"
    return "❌ Below margin target"