def competitor_reaction(price_change: float) -> str:
    if price_change > 0.05:
        return "Competitor likely holds price and waits."
    elif price_change < -0.05:
        return "Competitor may start a price war."
    else:
        return "Competitor may mirror the price within a day."

if __name__ == "__main__":
    delta = float(input("Enter your price change ($): "))
    print(competitor_reaction(delta))